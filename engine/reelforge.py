#!/usr/bin/env python3
"""
reelforge.py  --  HUNCH LAB  V0.1
=================================
Genera UN Reel completo de un experimento procedural con prediccion:
"Which ball wins?"  (carrera de bolas por una pista generada por semilla).

Salida (carpeta out/):
    hunch_<seed>.mp4      9:16, 1080x1920, 30 fps, H.264 + AAC 48 kHz, faststart
    hunch_<seed>_cover.jpg
    hunch_<seed>.json     metadatos (semilla, ganador, tiempos, caption)

Requisitos (todo gratis): Python 3.9+, Pillow >= 10.1, numpy, FFmpeg en el PATH.
Sin IA, sin APIs, sin musica de terceros: el audio se sintetiza con matematicas.

Uso:
    python reelforge.py --seed 7
    python reelforge.py --seed 7 --lang es --candidates 16
"""
import argparse
import bisect
import json
import math
import os
import random
import shutil
import subprocess
import sys
import time
import wave

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

# --------------------------------------------------------------------------
# CONFIG
# --------------------------------------------------------------------------
W, H = 1080, 1920
FPS = 30
SUB = 10                      # subpasos de fisica por frame
DT = 1.0 / (FPS * SUB)
SR = 48000                    # sample rate del audio

R_BALL = 36
GRAVITY = 1900.0
WALL_L, WALL_R = 44, 1036
TOP_Y = 790                   # y del extremo alto de la 1ra plataforma
N_LEVELS = 4
LEVEL_DY = 215
GAP = 150                     # hueco por donde cae la bola al siguiente nivel
T_MAX_RACE = 45.0             # segundos maximos de carrera simulada (despues del GO)
T_HOOK = 1.7                  # segundos de hook
T_COUNT = 0.7                 # segundos por numero de la cuenta atras
T_GO = T_HOOK + 3 * T_COUNT   # instante en que se abre la cubeta (3.8 s)
CHUTE_L, CHUTE_R, CHUTE_FLOOR, CHUTE_TOP = 395, 705, 470, 318

BALL_COLORS = [(255, 77, 109), (77, 212, 255), (255, 214, 10), (126, 255, 140)]
LETTERS = ["A", "B", "C", "D"]
PALETTES = [
    dict(top=(11, 14, 32), bot=(30, 16, 64), track=(226, 232, 255), peg=(150, 156, 214), glow=(44, 46, 96), tglow=(40, 46, 96)),
    dict(top=(6, 26, 34), bot=(12, 62, 72), track=(214, 255, 245), peg=(120, 200, 190), glow=(20, 70, 80), tglow=(18, 66, 76)),
    dict(top=(34, 12, 36), bot=(86, 28, 62), track=(255, 225, 240), peg=(214, 150, 190), glow=(80, 34, 70), tglow=(76, 32, 66)),
    dict(top=(8, 28, 20), bot=(24, 64, 42), track=(225, 255, 225), peg=(140, 200, 150), glow=(26, 70, 44), tglow=(24, 66, 42)),
]
for _p in PALETTES:
    _p["mid"] = tuple((a + b) // 2 for a, b in zip(_p["top"], _p["bot"]))
WHITE = (255, 255, 255)

# Recorridos: cada video combina tramos distintos (rampa / embudo / campo de postes)
COURSES = [
    ["ramp", "funnel", "ramp"], ["funnel", "ramp", "pegs"], ["pegs", "ramp", "funnel"],
    ["ramp", "ramp", "ramp"], ["ramp", "pegs", "funnel"], ["funnel", "pegs", "ramp"],
    ["ramp", "funnel", "pegs"], ["funnel", "ramp", "funnel"],
]
STAGE_H = {"ramp": 215, "funnel": 215, "pegs": 280}


def make_course(base_seed):
    """Recorrido largo (7-8 tramos) distinto para cada video."""
    r = random.Random(base_seed * 31 + 7)
    n = r.choice((7, 8))
    while True:
        seq = [r.choices(("ramp", "funnel", "pegs"), weights=(0.45, 0.35, 0.20))[0] for _ in range(n)]
        if seq.count("ramp") < 3 or seq.count("pegs") > 3:
            continue
        if any(seq[i] == seq[i + 1] == seq[i + 2] for i in range(n - 2)):
            continue
        return seq

TEXT = {
    "en": {
        "q": "WHICH BALL WINS?",
        "pick": "Pick before it drops",
        "comment": "Comment A, B or C",
        "go": "GO!",
        "wins": "{L} WINS",
        "by": "by {s:.2f} s",
        "did": "Did you guess it?",
        "daily": "New experiment daily",
        "caption": "Which ball wins? Pick {opts} before you watch, then tell me in the comments. "
                   "Did you get it right?",
        "tags": "#physics #satisfying #experiment #prediction #simulation",
    },
    "es": {
        "q": "¿QUÉ BOLA GANA?",
        "pick": "Elegí antes de que caiga",
        "comment": "Comentá A, B o C",
        "go": "¡YA!",
        "wins": "GANA {L}",
        "by": "por {s:.2f} s",
        "did": "¿Acertaste?",
        "daily": "Nuevo experimento cada día",
        "caption": "¿Qué bola gana? Elegí {opts} antes de mirar y contame en los comentarios. "
                   "¿Acertaste?",
        "tags": "#fisica #satisfactorio #experimento #prediccion #simulacion",
    },
}

HANDLE = "@hunch.lab"

# --------------------------------------------------------------------------
# FUENTES (sin archivos externos obligatorios)
# --------------------------------------------------------------------------
_FONT_CACHE = {}
_FONT_CANDIDATES = [
    "arialbd.ttf", "Arial Bold.ttf", "Arial Rounded Bold.ttf",
    "DejaVuSans-Bold.ttf", "LiberationSans-Bold.ttf", "FreeSansBold.ttf",
    "HelveticaNeue-Bold.ttf", "Helvetica-Bold.ttf", "Verdana Bold.ttf", "verdanab.ttf",
]


def get_font(size):
    size = int(size)
    if size in _FONT_CACHE:
        return _FONT_CACHE[size]
    font = None
    for name in _FONT_CANDIDATES:
        try:
            font = ImageFont.truetype(name, size)
            break
        except OSError:
            continue
    if font is None:
        try:
            font = ImageFont.load_default(size=size)   # Pillow >= 10.1
        except TypeError:
            font = ImageFont.load_default()
    _FONT_CACHE[size] = font
    return font


def fit_font(draw, text, max_w, start, min_size=24):
    size = start
    while size > min_size:
        f = get_font(size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 4
    return get_font(min_size)


def text_center(draw, text, cx, cy, font, fill=WHITE, stroke=6, stroke_fill=(8, 10, 24)):
    draw.text((cx, cy), text, font=font, fill=fill, anchor="mm",
              stroke_width=stroke, stroke_fill=stroke_fill)


# --------------------------------------------------------------------------
# GENERACION DE LA PISTA (determinista por semilla)
# --------------------------------------------------------------------------
def build_track(rng, course):
    """Devuelve (segmentos, circulos). Segmento=(x1,y1,x2,y2,grosor,e,mu,id); Circulo=(x,y,r,e,id).
    El recorrido se arma apilando tramos (rampa / embudo / campo de postes) con holgura garantizada."""
    segs, circs = [], []
    sid = 0
    floor_y = TOP_Y + sum(STAGE_H[k] for k in course) + 155
    segs.append((WALL_L, 300, WALL_L, floor_y, 6, 0.45, 0.0, sid)); sid += 1
    segs.append((WALL_R, 300, WALL_R, floor_y, 6, 0.45, 0.0, sid)); sid += 1
    segs.append((WALL_L, floor_y, WALL_R, floor_y, 6, 0.25, 0.05, sid)); sid += 1
    # cubeta de salida (la trampilla se maneja en la simulacion)
    segs.append((CHUTE_L, CHUTE_TOP, CHUTE_L, CHUTE_FLOOR, 6, 0.5, 0.0, sid)); sid += 1
    segs.append((CHUTE_R, CHUTE_TOP, CHUTE_R, CHUTE_FLOOR, 6, 0.5, 0.0, sid)); sid += 1
    # dispersion inicial
    for row, ry in enumerate((590, 685)):
        xs = range(150, 800, 112) if row % 2 == 0 else range(206, 760, 112)
        for px in xs:
            circs.append((float(px), float(ry), 16.0, 0.72, sid)); sid += 1

    y = TOP_Y
    exit_x = None
    marks = []
    for kind in course:
        if kind == "ramp":
            d = rng.choice((1, -1)) if exit_x is None else (1 if exit_x < W / 2 else -1)
            gap = rng.uniform(140, 185)
            slope = math.radians(rng.uniform(5.0, 7.4))
            x1, x2 = (WALL_L, WALL_R - gap) if d > 0 else (WALL_R, WALL_L + gap)
            y2 = y + abs(x2 - x1) * math.tan(slope)
            segs.append((x1, y, x2, y2, 6, 0.30, 0.0009, sid)); sid += 1
            exit_x = (x2 + (WALL_R if d > 0 else WALL_L)) / 2
            marks.append((exit_x, y2))
        elif kind == "funnel":
            hx = rng.uniform(300, 780)
            hw = rng.uniform(56, 70)
            segs.append((WALL_L, y, hx - hw, y + 95, 6, 0.30, 0.0009, sid)); sid += 1
            segs.append((WALL_R, y, hx + hw, y + 95, 6, 0.30, 0.0009, sid)); sid += 1
            exit_x = hx
            marks.append((hx, y + 95))
        else:  # pegs
            hs = rng.uniform(128, 150)
            for row in (0, 1):
                ry = y + 60 + row * 100
                x = 150 + (hs / 2 if row else 0)
                while x <= WALL_R - 150 + 1:
                    if rng.random() > 0.15:
                        r = rng.uniform(13, 18)
                        circs.append((x, ry, r, rng.uniform(0.6, 0.9), sid)); sid += 1
                    x += hs
            exit_x = None
        y += STAGE_H[kind]
    return segs, circs, floor_y, marks


def build_buckets(segs, circs):
    buckets = {}
    def add(obj, kind, ymin, ymax):
        for b in range(int((ymin - 90) // 100), int((ymax + 90) // 100) + 1):
            buckets.setdefault(b, []).append((kind, obj))
    for s in segs:
        add(s, "s", min(s[1], s[3]), max(s[1], s[3]))
    for c in circs:
        add(c, "c", c[1] - c[2], c[1] + c[2])
    return buckets


# --------------------------------------------------------------------------
# SIMULACION
# --------------------------------------------------------------------------
def simulate(seed, course=0, palette=0, n_balls=3, allow_partial=False):
    rng = random.Random(seed)
    segs, circs, floor_y, marks = build_track(rng, course)
    finish_y = floor_y - 70
    pulses = []
    buckets = build_buckets(segs, circs)

    # posiciones iniciales (slots) y letras barajadas -> sin sesgo por posicion
    slots = [465 + i * 90 for i in range(n_balls)]
    order = list(range(n_balls))
    rng.shuffle(order)
    balls = []
    for slot_i, x in enumerate(slots):
        balls.append({
            "x": x + rng.uniform(-6, 6), "y": 395.0 + rng.uniform(-3, 3),
            "vx": rng.uniform(-30, 30), "vy": 0.0, "r": R_BALL,
            "id": order[slot_i], "fin": None,
        })

    frames = []          # frames[k] = [(x,y)] por bola
    events = []          # (t, kind, speed, x, obj_id)
    first_y = [b["y"] for b in balls]
    t = 0.0
    k = 0
    leader_hist = []
    max_frames = int((T_GO + T_MAX_RACE) * FPS)
    next_pulse = 1.0
    while k < max_frames:
        frames.append([(b["x"], b["y"]) for b in balls])
        # lider por progreso (y)
        lead = max(range(n_balls), key=lambda i: balls[i]["y"])
        leader_hist.append((lead, sorted(b["y"] for b in balls)[-1] - sorted(b["y"] for b in balls)[-2]))
        if t < T_GO and any(b["x"] < CHUTE_L - 5 or b["x"] > CHUTE_R + 5 or b["y"] > CHUTE_FLOOR + 6
                            for b in balls):
            return None            # una bola se escapo de la cubeta antes del GO: candidato invalido
        if all(b["fin"] is not None for b in balls):
            break
        for _ in range(SUB):
            t += DT
            if T_HOOK * 0.55 <= t < T_GO and t >= next_pulse:
                next_pulse += rng.uniform(0.16, 0.30)       # sacudon: salto + empujon lateral
                pulses.append(t)
                for b in balls:
                    if b["y"] > CHUTE_FLOOR - 52:                          # solo patea a las apoyadas
                        b["vy"] = -rng.uniform(300, 560)
                        b["vx"] = max(-420.0, min(420.0, b["vx"] + rng.uniform(-260, 260)))
            for b in balls:
                if t < T_GO:   # trampilla cerrada
                    hit = _segment(b, CHUTE_L, CHUTE_FLOOR, CHUTE_R, CHUTE_FLOOR, 6, 0.35, 0.002)
                    if hit > 260:
                        events.append((t, "seg", hit, b["x"], 9999))
            for b in balls:
                b["vy"] += GRAVITY * DT
                b["vx"] *= 0.99985
                sp = math.hypot(b["vx"], b["vy"])
                if sp > 2000:
                    b["vx"] *= 2000 / sp
                    b["vy"] *= 2000 / sp
                b["x"] += b["vx"] * DT
                b["y"] += b["vy"] * DT
                bi = int(b["y"] // 100)
                for kind, o in buckets.get(bi, ()):
                    if kind == "c":
                        cx, cy, cr, e, oid = o
                        hit = _circle(b, cx, cy, cr, e)
                        if hit > 140:
                            events.append((t, "peg", hit, b["x"], oid))
                    else:
                        x1, y1, x2, y2, th, e, mu, oid = o
                        hit = _segment(b, x1, y1, x2, y2, th, e, mu)
                        if hit > 260:
                            events.append((t, "seg", hit, b["x"], oid))
                if b["fin"] is None and b["y"] >= finish_y and t > T_GO:
                    b["fin"] = t
            # bola-bola
            for i in range(n_balls):
                for j in range(i + 1, n_balls):
                    hit = _ball_ball(balls[i], balls[j])
                    if hit > 120:
                        events.append((t, "bb", hit, (balls[i]["x"] + balls[j]["x"]) / 2, 0))
        k += 1

    fins = [b["fin"] for b in balls]
    if any(f is None for f in fins) and not allow_partial:
        return None
    return {
        "seed": seed, "n": n_balls, "frames": frames, "events": events,
        "fin": fins, "ids": [b["id"] for b in balls], "segs": segs, "circs": circs, "pulses": pulses,
        "course": course, "palette": palette, "floor_y": floor_y, "finish_y": finish_y, "marks": marks,
        "leader_hist": leader_hist,
    }


def _circle(b, cx, cy, cr, e):
    dx, dy = b["x"] - cx, b["y"] - cy
    rr = b["r"] + cr
    d2 = dx * dx + dy * dy
    if d2 >= rr * rr:
        return 0.0
    d = math.sqrt(d2) or 1e-6
    nx, ny = dx / d, dy / d
    pen = rr - d
    b["x"] += nx * pen
    b["y"] += ny * pen
    vn = b["vx"] * nx + b["vy"] * ny
    if vn < 0:
        b["vx"] -= (1 + e) * vn * nx
        b["vy"] -= (1 + e) * vn * ny
        return -vn
    return 0.0


def _segment(b, x1, y1, x2, y2, th, e, mu):
    sx, sy = x2 - x1, y2 - y1
    l2 = sx * sx + sy * sy
    t = ((b["x"] - x1) * sx + (b["y"] - y1) * sy) / l2
    t = 0.0 if t < 0 else 1.0 if t > 1 else t
    px, py = x1 + sx * t, y1 + sy * t
    dx, dy = b["x"] - px, b["y"] - py
    rr = b["r"] + th
    d2 = dx * dx + dy * dy
    if d2 >= rr * rr:
        return 0.0
    d = math.sqrt(d2) or 1e-6
    nx, ny = dx / d, dy / d
    pen = rr - d
    b["x"] += nx * pen
    b["y"] += ny * pen
    vn = b["vx"] * nx + b["vy"] * ny
    if vn < 0:
        b["vx"] -= (1 + e) * vn * nx
        b["vy"] -= (1 + e) * vn * ny
        # friccion tangencial
        tx, ty = -ny, nx
        vt = b["vx"] * tx + b["vy"] * ty
        b["vx"] -= mu * vt * tx
        b["vy"] -= mu * vt * ty
        return -vn
    return 0.0


def _ball_ball(a, c):
    dx, dy = c["x"] - a["x"], c["y"] - a["y"]
    rr = a["r"] + c["r"]
    d2 = dx * dx + dy * dy
    if d2 >= rr * rr:
        return 0.0
    d = math.sqrt(d2) or 1e-6
    nx, ny = dx / d, dy / d
    pen = (rr - d) / 2
    a["x"] -= nx * pen; a["y"] -= ny * pen
    c["x"] += nx * pen; c["y"] += ny * pen
    rvx, rvy = c["vx"] - a["vx"], c["vy"] - a["vy"]
    vn = rvx * nx + rvy * ny
    if vn < 0:
        j = -(1 + 0.8) * vn / 2
        a["vx"] -= j * nx; a["vy"] -= j * ny
        c["vx"] += j * nx; c["vy"] += j * ny
        return -vn
    return 0.0


def tension_score(sim):
    """Curadoria algoritmica: elegimos la semilla mas 'emocionante'."""
    fins = sorted(sim["fin"])
    t_last = fins[-1]
    gap = fins[1] - fins[0]
    lead = 0
    prev = None
    for l, margin in sim["leader_hist"][int(T_GO * FPS):]:
        if margin < 18:
            continue
        if prev is not None and l != prev:
            lead += 1
        prev = l
    s_time = max(0.0, 1 - abs((t_last - T_GO) - 18.0) / 9.0)
    s_gap = math.exp(-gap / 0.6)
    s_lead = min(lead, 4) / 4
    return 1.2 * s_gap + 1.0 * s_time + 0.8 * s_lead, {
        "race_s": round(t_last - T_GO, 2), "gap": round(gap, 3), "lead_changes": lead}


# --------------------------------------------------------------------------
# RENDER
# --------------------------------------------------------------------------
def vgradient(pal, h=H):
    t = np.linspace(0, 1, h)[:, None, None]
    top = np.array(pal['top'], dtype=np.float32)[None, None, :]
    bot = np.array(pal['bot'], dtype=np.float32)[None, None, :]
    img = top * (1 - t) + bot * t
    img = np.repeat(img, W, axis=1)
    # vineta suave
    yy, xx = np.mgrid[0:h, 0:W].astype(np.float32)
    d = np.sqrt(((xx - W / 2) / (W * 0.75)) ** 2 + ((yy % H - H / 2) / (H * 0.75)) ** 2)
    img *= (1.0 - 0.35 * np.clip(d, 0, 1) ** 2)[:, :, None]
    return Image.fromarray(np.clip(img, 0, 255).astype(np.uint8), "RGB")


def thick_line(draw, x1, y1, x2, y2, w, fill, s):
    draw.line([(x1 * s, y1 * s), (x2 * s, y2 * s)], fill=fill, width=int(w * s))
    for (x, y) in ((x1, y1), (x2, y2)):
        r = w * s / 2
        draw.ellipse([x * s - r, y * s - r, x * s + r, y * s + r], fill=fill)


def mix(c1, c2, a):
    return tuple(int(c1[i] * (1 - a) + c2[i] * a) for i in range(3))


ACCENTS = [(255, 77, 109), (77, 212, 255), (255, 214, 10)]


def build_static(sim):
    """Fondo + pista con detalle, dibujado a 2x y reducido (antialias)."""
    S = 2
    pal = PALETTES[sim['palette']]
    wh = sim['floor_y'] + 265
    fy = sim['finish_y']
    rng = random.Random(sim['seed'] * 13 + 5)
    bg = vgradient(pal, wh).resize((W * S, wh * S), Image.BILINEAR).convert("RGBA")

    # luces difusas (bokeh) + resplandor de la meta
    layer = Image.new("RGBA", (W, wh), (0, 0, 0, 0))
    ld = ImageDraw.Draw(layer)
    for _ in range(int(wh / 210)):
        x, y, r = rng.uniform(0, W), rng.uniform(0, wh), rng.uniform(55, 140)
        ld.ellipse([x - r, y - r, x + r, y + r], fill=mix(pal['track'], rng.choice(ACCENTS), 0.55) + (38,))
    ld.rectangle([WALL_L, fy - 30, WALL_R, fy + 60], fill=(255, 255, 255, 46))
    layer = layer.filter(ImageFilter.GaussianBlur(30))
    bg = Image.alpha_composite(bg, layer.resize((W * S, wh * S), Image.BILINEAR))

    # cuadricula tipo plano de laboratorio
    grid = Image.new("RGBA", (W * S, wh * S), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    for gx in range(0, W + 1, 90):
        gd.line([(gx * S, 0), (gx * S, wh * S)], fill=(255, 255, 255, 15), width=S)
    for gy in range(0, wh + 1, 90):
        gd.line([(0, gy * S), (W * S, gy * S)], fill=(255, 255, 255, 15), width=S)
    bg = Image.alpha_composite(bg, grid)
    d = ImageDraw.Draw(bg)

    # marcadores de profundidad en las paredes
    dim = mix(pal['track'], pal['mid'], 0.55)
    f_small = get_font(24 * S)
    k = 0
    for y in range(TOP_Y, int(fy), 200):
        d.line([(WALL_L * S + 8 * S, y * S), (WALL_L * S + 34 * S, y * S)], fill=dim, width=2 * S)
        d.line([(WALL_R * S - 34 * S, y * S), (WALL_R * S - 8 * S, y * S)], fill=dim, width=2 * S)
        d.text(((WALL_L + 42) * S, y * S), f"{k * 10} m", font=f_small, fill=dim, anchor="lm")
        k += 1

    shadow_col = mix(pal['top'], (0, 0, 0), 0.55)
    # carriles: sombra, resplandor, riel, brillo superior y remaches
    for x1, y1, x2, y2, th, e, mu, oid in sim["segs"]:
        thick_line(d, x1 + 3, y1 + 11, x2 + 3, y2 + 11, th * 2 + 6, shadow_col, S)
    for x1, y1, x2, y2, th, e, mu, oid in sim["segs"]:
        thick_line(d, x1, y1, x2, y2, th * 2 + 12, pal['tglow'], S)
    for x1, y1, x2, y2, th, e, mu, oid in sim["segs"]:
        thick_line(d, x1, y1, x2, y2, th * 2, pal['track'], S)
        if abs(x2 - x1) > 2:
            thick_line(d, x1, y1 - 3, x2, y2 - 3, 2.2, mix(pal['track'], WHITE, 0.75), S)
            L = math.hypot(x2 - x1, y2 - y1)
            for j in range(int(L // 70)):
                u = (j + 0.5) * 70 / L
                rx, ry = x1 + (x2 - x1) * u, y1 + (y2 - y1) * u
                r = 3.2 * S
                d.ellipse([rx * S - r, ry * S - r, rx * S + r, ry * S + r], fill=mix(pal['track'], pal['bot'], 0.55))

    # postes: sombra, aro, cuerpo, brillo y tapa de color
    for cx, cy, cr, e, oid in sim["circs"]:
        r = (cr + 5) * S
        d.ellipse([cx * S - r + 4 * S, cy * S - r + 8 * S, cx * S + r + 4 * S, cy * S + r + 8 * S], fill=shadow_col)
        r = (cr + 8) * S
        d.ellipse([cx * S - r, cy * S - r, cx * S + r, cy * S + r], fill=pal['glow'])
        r = cr * S
        d.ellipse([cx * S - r, cy * S - r, cx * S + r, cy * S + r], fill=pal['peg'],
                  outline=mix(pal['peg'], WHITE, 0.55), width=2 * S)
        r = cr * 0.42 * S
        d.ellipse([cx * S - r - 3 * S, cy * S - r - 3 * S, cx * S + r - 3 * S, cy * S + r - 3 * S], fill=(228, 232, 255))
        if oid % 3 == 0:
            r = cr * 0.30 * S
            d.ellipse([cx * S - r + 2 * S, cy * S - r + 3 * S, cx * S + r + 2 * S, cy * S + r + 3 * S],
                      fill=ACCENTS[(oid // 3) % 3])

    # flechas hacia donde caen las bolas (agujeros y huecos)
    for mx, my in sim["marks"]:
        for j in range(2):
            y0 = my + 30 + j * 30
            col = mix(pal['track'], ACCENTS[1], 0.45 - 0.2 * j)
            d.line([((mx - 22) * S, y0 * S), (mx * S, (y0 + 17) * S), ((mx + 22) * S, y0 * S)],
                   fill=col, width=6 * S, joint="curve")

    # cubeta de salida: lamparas
    for px in (CHUTE_L, CHUTE_R):
        r = 10 * S
        d.ellipse([px * S - r, CHUTE_TOP * S - r, px * S + r, CHUTE_TOP * S + r], fill=ACCENTS[2],
                  outline=WHITE, width=2 * S)

    # meta: damero, banderas y cartel
    sq = 22
    for i in range(int((WALL_R - WALL_L) // sq)):
        for j in range(2):
            col = (255, 255, 255) if (i + j) % 2 == 0 else (20, 22, 46)
            x0 = WALL_L + i * sq
            y0 = fy + 6 + j * sq
            d.rectangle([x0 * S, y0 * S, (x0 + sq) * S, (y0 + sq) * S], fill=col)
    for px, sgn, col in ((WALL_L + 46, 1, ACCENTS[0]), (WALL_R - 46, -1, ACCENTS[1])):
        d.line([(px * S, (fy - 120) * S), (px * S, (fy + 6) * S)], fill=pal['track'], width=5 * S)
        d.polygon([(px * S, (fy - 120) * S), ((px + 56 * sgn) * S, (fy - 100) * S), (px * S, (fy - 80) * S)], fill=col)
    d.text((W / 2 * S, (fy - 52) * S), "F I N I S H", font=get_font(46 * S), fill=mix(pal['track'], pal['mid'], 0.35),
           anchor="mm")
    return bg.convert("RGB").resize((W, wh), Image.LANCZOS)


EXTRA = {}


def make_extras():
    R = R_BALL
    size = int(R * 4)
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    dist = np.sqrt((xx - size / 2) ** 2 + (yy - size / 2) ** 2) / (size / 2)
    a = (np.clip(1 - dist, 0, 1) ** 2 * 150).astype(np.uint8)
    glows = []
    for col in BALL_COLORS:
        arr = np.dstack([np.full((size, size), col[0], np.uint8), np.full((size, size), col[1], np.uint8),
                         np.full((size, size), col[2], np.uint8), a])
        glows.append(Image.fromarray(arr, "RGBA"))
    sh = Image.new("RGBA", (2 * R + 44, 2 * R + 44), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse([22, 26, 22 + 2 * R, 26 + 2 * R], fill=(0, 0, 0, 120))
    sh = sh.filter(ImageFilter.GaussianBlur(8))
    ta = np.linspace(150, 0, 380).astype(np.uint8)[:, None].repeat(W, axis=1)
    top = Image.fromarray(np.dstack([np.zeros((380, W), np.uint8)] * 3 + [ta]), "RGBA")
    ba = np.linspace(0, 175, 300).astype(np.uint8)[:, None].repeat(W, axis=1)
    bot = Image.fromarray(np.dstack([np.zeros((300, W), np.uint8)] * 3 + [ba]), "RGBA")
    EXTRA.update(glow=glows, shadow=sh, top=top, bottom=bot)


def make_ball_sprite(color, letter):
    S = 4
    R = R_BALL
    size = (2 * R + 8) * S
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    yy, xx = np.mgrid[0:size, 0:size].astype(np.float32)
    c = size / 2
    dist = np.sqrt((xx - c) ** 2 + (yy - c) ** 2) / (R * S)
    hl = np.sqrt((xx - (c - R * S * 0.35)) ** 2 + (yy - (c - R * S * 0.4)) ** 2) / (R * S)
    shade = 0.62 + 0.55 * np.clip(1 - hl, 0, 1) ** 1.6 - 0.18 * np.clip(dist, 0, 1) ** 3
    col = np.array(color, dtype=np.float32)[None, None, :] * shade[:, :, None]
    col = np.clip(col, 0, 255).astype(np.uint8)
    alpha = (dist <= 1.0).astype(np.uint8) * 255
    arr = np.dstack([col, alpha])
    img = Image.fromarray(arr, "RGBA")
    d = ImageDraw.Draw(img)
    f = get_font(int(R * 1.15 * S))
    d.text((c, c + 2 * S), letter, font=f, fill=(20, 22, 40, 255), anchor="mm")
    return img.resize((2 * R + 8, 2 * R + 8), Image.LANCZOS)


def lerp(a, b, t):
    return a + (b - a) * t


class Timeline:
    def __init__(self, sim):
        self.sim = sim
        self.t_hook = T_HOOK
        self.t_count_len = T_COUNT
        self.t_go = T_GO
        fins = sorted(sim["fin"])
        self.t_first = fins[0]
        self.t_last_fin = fins[-1]
        self.t_sim_end = self.t_last_fin + 0.5
        self.t_cta = self.t_sim_end + 0.9
        self.t_total = self.t_cta + 2.7
        self.loop_len = 0.7
        self.n_frames = int(round(self.t_total * FPS))

    def frame_idx(self, t):
        k = int(t * FPS)
        return max(0, min(k, len(self.sim["frames"]) - 1))


def compute_cams(sim):
    """Camara que sigue a las bolas (el lider siempre queda a la vista)."""
    frames = sim["frames"]
    cam_max = sim["floor_y"] + 265 - H
    n_pre = int(T_GO * FPS)
    cams, cs = [], 0.0
    for k, pos in enumerate(frames):
        ys = [p[1] for p in pos]
        if k < n_pre:
            target = 0.0
        else:
            target = min(max(max(sum(ys) / len(ys) - 1000, max(ys) - 1600), 0.0), cam_max)
        cs += (target - cs) * 0.10
        cs = max(cs, min(max(max(ys) - 1620, 0.0), cam_max))
        cams.append(min(cs, cam_max))
    return cams


CONFETTI_COLORS = [(255, 77, 109), (77, 212, 255), (255, 214, 10), (126, 255, 140), (255, 255, 255)]


def prepare_decor(sim, base_seed):
    """Datos deterministas para los efectos (particulas, confeti, destellos de postes)."""
    r = random.Random(base_seed * 3 + 1)
    sim["particles"] = [(r.uniform(0, W), r.uniform(0, H), r.uniform(1.5, 4.5), r.uniform(8, 30),
                         r.uniform(0, 6.28)) for _ in range(34)]
    sim["confetti"] = [(r.uniform(0, 0.9), r.uniform(0, W), r.uniform(320, 640), r.uniform(15, 55),
                        r.uniform(0, 6.28), r.uniform(10, 19), r.randrange(len(CONFETTI_COLORS)),
                        r.uniform(-7, 7)) for _ in range(70)]
    hits = sorted((te, oid, sp) for (te, kind, sp, x, oid) in sim["events"] if kind == "peg" and te >= T_GO)
    sim["_peg_hits"] = hits
    sim["_peg_t"] = [h[0] for h in hits]
    sim["_peg_pos"] = {c[4]: (c[0], c[1], c[2]) for c in sim["circs"]}
    sim["exp_no"] = base_seed


def render_frame(t, sim, tl, static, sprites, tx, order_letters, winner_i, margin):
    k = tl.frame_idx(t)
    oy = int(round(sim["cams"][k]))
    img = static.crop((0, oy, W, oy + H))
    d = ImageDraw.Draw(img)
    pal = PALETTES[sim['palette']]
    mid = pal['mid']
    n = sim["n"]
    cx = W // 2
    racing = t >= tl.t_go
    pos = [(x, y - oy) for (x, y) in sim["frames"][k]]

    # ---- particulas ambientales (parallax suave)
    for (x0, y0, sz, sp, ph) in sim["particles"]:
        x = (x0 + 25 * math.sin(t * 0.6 + ph)) % W
        y = (y0 - 0.3 * oy - t * sp) % H
        a = 0.16 + 0.30 * (0.5 + 0.5 * math.sin(t * 2.2 + ph))
        d.ellipse([x - sz, y - sz, x + sz, y + sz], fill=mix(mid, WHITE, a))

    # ---- trampilla de la cubeta (antes del GO)
    if t < tl.t_go:
        yy = CHUTE_FLOOR + 3 - oy
        d.line([(CHUTE_L, yy), (CHUTE_R, yy)], fill=(255, 190, 90), width=10)
        for px in (CHUTE_L + 14, CHUTE_R - 14):
            d.ellipse([px - 6, yy - 6, px + 6, yy + 6], fill=(255, 240, 200))

    # ---- destellos al pegar en los postes
    if racing:
        times = sim["_peg_t"]
        lo = bisect.bisect_left(times, t - 0.35)
        hi = bisect.bisect_right(times, t)
        for j in range(lo, hi):
            te, oid, speed = sim["_peg_hits"][j]
            px, py, pr = sim["_peg_pos"][oid]
            ys = py - oy
            if ys < -90 or ys > H + 90:
                continue
            age = t - te
            f = age / 0.35
            if age < 0.12:
                rr = pr + 4
                d.ellipse([px - rr, ys - rr, px + rr, ys + rr], fill=mix(pal['peg'], WHITE, 0.9))
            rr = pr + 6 + age * 230
            d.ellipse([px - rr, ys - rr, px + rr, ys + rr], outline=mix(mid, pal['track'], (1 - f) ** 1.4 * 0.9), width=3)
            rnd = random.Random(oid * 977 + int(te * 1000))
            for _ in range(5):
                ang = rnd.uniform(0, 6.283)
                dist = pr + age * rnd.uniform(120, 260)
                sx, sy = px + math.cos(ang) * dist, ys + math.sin(ang) * dist
                sz = 4.5 * (1 - f)
                d.ellipse([sx - sz, sy - sz, sx + sz, sy + sz], fill=mix(mid, WHITE, 1 - f))

    # ---- estelas
    if racing and t < tl.t_sim_end + 0.4:
        for i in range(n):
            col = BALL_COLORS[sim_ball_color(sim, i)]
            for m in range(1, 9):
                kk = max(0, k - m * 2)
                x, y = sim["frames"][kk][i]
                y -= oy
                a = (1 - m / 9) * 0.45
                c = mix(mid, col, a)
                r = R_BALL * (1 - m / 12)
                d.ellipse([x - r, y - r, x + r, y + r], fill=c)

    # ---- bolas: sombra, resplandor, cuerpo
    pulse = 1.0
    if t < tl.t_go:
        pulse = 1.0 + 0.04 * math.sin(t * 7)
    for i in range(n):
        x, y = pos[i]
        cid = sim_ball_color(sim, i)
        sh = EXTRA["shadow"]
        img.paste(sh, (int(x - sh.width / 2 + 4), int(y - sh.height / 2 + 6)), sh)
        gl = EXTRA["glow"][cid]
        img.paste(gl, (int(x - gl.width / 2), int(y - gl.height / 2)), gl)
        spr = sprites[cid]
        if abs(pulse - 1.0) > 1e-3:
            sz = int(spr.width * pulse)
            spr_i = spr.resize((sz, sz), Image.BILINEAR)
        else:
            spr_i = spr
        img.paste(spr_i, (int(x - spr_i.width / 2), int(y - spr_i.height / 2)), spr_i)

    # ---- ganadora: aro + corona
    if winner_i is not None and t >= tl.t_first:
        x, y = pos[winner_i]
        ph = (t - tl.t_first) * 3.0
        r = R_BALL + 10 + 6 * math.sin(ph * 2)
        d.ellipse([x - r, y - r, x + r, y + r], outline=WHITE, width=5)
        by = y - R_BALL - 16 + 4 * math.sin(ph * 2)
        crown = [(x - 22, by), (x - 22, by - 24), (x - 11, by - 11), (x, by - 30), (x + 11, by - 11),
                 (x + 22, by - 24), (x + 22, by)]
        d.polygon(crown, fill=(255, 214, 10), outline=WHITE)

    # ---- minimapa de progreso (derecha)
    if racing:
        bx = 1060
        d.line([(bx, 380), (bx, 1640)], fill=mix(mid, WHITE, 0.28), width=5)
        for yy in range(380, 1641, 180):
            d.line([(bx - 8, yy), (bx + 8, yy)], fill=mix(mid, WHITE, 0.28), width=3)
        for i in range(n):
            py = sim["frames"][k][i][1]
            prog = min(1.0, max(0.0, (py - 420) / (sim["finish_y"] - 420)))
            by = 380 + prog * 1260
            col = BALL_COLORS[sim_ball_color(sim, i)]
            d.ellipse([bx - 11, by - 11, bx + 11, by + 11], fill=col, outline=WHITE, width=2)
        for q in range(4):
            d.rectangle([bx - 12 + q * 6, 1646, bx - 6 + q * 6, 1652], fill=WHITE if q % 2 == 0 else (20, 22, 46))

    # ---- confeti tras la meta
    if winner_i is not None and t >= tl.t_first:
        for (delay, x0, vy, amp, ph, size, ci, rot) in sim["confetti"]:
            age = t - tl.t_first - delay
            if age < 0:
                continue
            y = -30 + age * vy
            if y > H + 30:
                continue
            x = x0 + amp * math.sin(age * 3 + ph)
            ang = age * rot
            c, sn = math.cos(ang), math.sin(ang)
            w2, h2 = size / 2, size / 4
            pts = [(x + px * c - py * sn, y + px * sn + py * c) for (px, py) in
                   ((-w2, -h2), (w2, -h2), (w2, h2), (-w2, h2))]
            d.polygon(pts, fill=CONFETTI_COLORS[ci])

    # ---- velos para que los textos se lean sobre la pista
    img.paste(EXTRA["top"], (0, 0), EXTRA["top"])
    img.paste(EXTRA["bottom"], (0, H - 300), EXTRA["bottom"])
    d = ImageDraw.Draw(img)

    # ---- etiqueta superior (marca + numero de experimento)
    label = f"HUNCH.LAB  ·  EXPERIMENT #{sim['exp_no']:02d}"
    f = get_font(34)
    tw = d.textlength(label, font=f)
    pw, ph_h = tw + 64, 56
    x0, y0 = cx - pw / 2, 46
    d.rounded_rectangle([x0, y0, x0 + pw, y0 + ph_h], radius=28, fill=mix(pal['top'], (0, 0, 0), 0.35),
                        outline=mix(pal['track'], mid, 0.35), width=2)
    d.text((cx, y0 + ph_h / 2 + 1), label, font=f, fill=pal['track'], anchor="mm")

    # ---- textos
    q_font = fit_font(d, tx["q"], W - 120, 118)
    if t < tl.t_go:
        text_center(d, tx["q"], cx, 185, q_font)
        sub = tx["pick"] if t < tl.t_hook else tx["comment"]
        text_center(d, sub, cx, 310, fit_font(d, sub, W - 140, 60), fill=(190, 205, 255), stroke=5)
        if t >= tl.t_hook:
            idx = int((t - tl.t_hook) / tl.t_count_len)
            phs = ((t - tl.t_hook) % tl.t_count_len) / tl.t_count_len
            num = str(3 - min(idx, 2))
            size = int(300 * (1.15 - 0.25 * phs))
            text_center(d, num, cx, 1000, get_font(size), fill=WHITE, stroke=10)
    elif t < tl.t_first:
        text_center(d, tx["q"], cx, 175, fit_font(d, tx["q"], W - 140, 96))
        if t < tl.t_go + 0.6:
            text_center(d, tx["go"], cx, 1000, get_font(260), fill=(126, 255, 140), stroke=10)
    elif t < tl.t_cta:
        text_center(d, tx["did"], cx, 185, fit_font(d, tx["did"], W - 140, 100))
        col = BALL_COLORS[sim_ball_color(sim, winner_i)]
        wl = tx["wins"].format(L=order_letters[winner_i])
        text_center(d, wl, cx, 1760, fit_font(d, wl, W - 100, 170), fill=col, stroke=9)
        text_center(d, tx["by"].format(s=margin), cx, 1860, get_font(58), fill=(200, 212, 255), stroke=5)
    else:
        text_center(d, tx["did"], cx, 195, fit_font(d, tx["did"], W - 140, 118))
        text_center(d, tx["comment"], cx, 1745, fit_font(d, tx["comment"], W - 120, 96), stroke=8)
        text_center(d, tx["daily"] + "  ·  " + HANDLE, cx, 1850,
                    fit_font(d, tx["daily"] + "  ·  " + HANDLE, W - 100, 52), fill=(190, 205, 255), stroke=4)

    if tl.t_go <= t < tl.t_first:
        text_center(d, HANDLE, cx, 1880, get_font(40), fill=(170, 185, 235), stroke=3)
    return img


def sim_ball_color(sim, i):
    return sim["ids"][i]   # color/letra de la bola i (letras barajadas respecto de la posicion)


# --------------------------------------------------------------------------
# AUDIO (sintesis pura: notas suaves tipo marimba/kalimba + eco; sin samples ni musica ajena)
# --------------------------------------------------------------------------
ROOTS = [261.63, 293.66, 349.23, 392.00, 329.63]      # do, re, fa, sol, mi (tono distinto por video)
MAJ_PENTA = [0, 2, 4, 7, 9]                           # escala pentatonica mayor: nunca suena "mal"


def pent_hz(root, idx):
    octv, deg = divmod(idx % 10, 5)
    return root * 2 ** ((MAJ_PENTA[deg] + 12 * octv) / 12.0)


def _pan(buf, i0, w, pan):
    n = len(w)
    buf[i0:i0 + n, 0] += w * math.cos(pan * math.pi / 2)
    buf[i0:i0 + n, 1] += w * math.sin(pan * math.pi / 2)


def mallet(buf, t0, freq, amp, pan=0.5):
    """Nota suave tipo marimba: fundamental calida + parcial breve, ataque sin click."""
    i0 = int(t0 * SR)
    if i0 < 0 or i0 >= buf.shape[0]:
        return
    n = min(int(1.5 * SR), buf.shape[0] - i0)
    tt = np.arange(n) / SR
    dec = 0.50 * (440.0 / freq) ** 0.25
    w = (np.sin(2 * np.pi * freq * tt) * np.exp(-tt / dec)
         + 0.16 * np.sin(2 * np.pi * freq * 3.9 * tt) * np.exp(-tt / (dec * 0.22))
         + 0.05 * np.sin(2 * np.pi * freq * 9.0 * tt) * np.exp(-tt / (dec * 0.08)))
    w *= np.minimum(1.0, tt / 0.006) * amp
    _pan(buf, i0, w, pan)


def bloop(buf, t0, f0, f1, dur, amp, pan=0.5):
    """Burbuja suave (para el sacudon y los choques entre bolas)."""
    i0 = int(t0 * SR)
    if i0 < 0 or i0 >= buf.shape[0]:
        return
    n = min(int(dur * SR), buf.shape[0] - i0)
    tt = np.arange(n) / SR
    f = f0 + (f1 - f0) * (tt / dur)
    w = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / (dur * 0.35)) * np.minimum(1.0, tt / 0.008) * amp
    _pan(buf, i0, w, pan)


def reverb(x, seed, wet=0.34, rt=1.2):
    """Eco de sala suave (respuesta al impulso sintetica, convolucion por FFT)."""
    n = int(rt * SR)
    tt = np.arange(n) / SR
    out = np.zeros_like(x)
    pre = int(0.018 * SR)
    for ch in range(2):
        r = np.random.default_rng(seed + ch)
        ir = r.standard_normal(n) * np.exp(-tt / (rt / 4.6))
        ir = np.convolve(ir, np.ones(7) / 7.0, mode="same")      # filtro: sin agudos duros
        ir[:pre] = 0
        ir /= np.sqrt(np.sum(ir ** 2)) + 1e-9
        L = len(x) + n
        N = 1 << (L - 1).bit_length()
        y = np.fft.irfft(np.fft.rfft(x[:, ch], N) * np.fft.rfft(ir, N), N)[:len(x)]
        out[:, ch] = y
    return x + wet * out


def synth_audio(sim, tl, path, seed=0):
    total = tl.t_total
    buf = np.zeros((int(total * SR) + SR, 2), dtype=np.float64)
    root = ROOTS[seed % len(ROOTS)]
    tt = np.arange(buf.shape[0]) / SR

    # colchon calido muy bajo (acorde mayor con vibrato lento)
    pad = sum(np.sin(2 * np.pi * f * tt) for f in (root / 2, root / 2 * 1.25, root / 2 * 1.5))
    pad *= 0.010 * (1 + 0.25 * np.sin(2 * np.pi * 0.22 * tt))
    pad *= np.minimum(1.0, tt / 1.5) * np.minimum(1.0, np.maximum(0.0, total - tt) / 1.0)
    buf[:, 0] += pad
    buf[:, 1] += pad

    # sacudon de la cubeta: burbujas suaves
    for p in sim.get("pulses", []):
        bloop(buf, p, 220, 150, 0.12, 0.05, pan=0.3 + 0.4 * ((p * 7.3) % 1))

    # cuenta regresiva: tres notas ascendentes + acorde en el GO
    base = root * 2
    for i, ratio in enumerate((1.0, 1.25, 1.5)):
        mallet(buf, tl.t_hook + i * tl.t_count_len, base * ratio, 0.20)
    for ratio in (1.0, 1.25, 1.5, 2.0):
        mallet(buf, tl.t_go, base * ratio, 0.13)

    # carrera: cada poste toca una nota de la escala
    last = {}
    win_count = {}
    for (te, kind, speed, x, oid) in sorted(sim["events"], key=lambda e: e[0]):
        if te < T_GO or te >= tl.t_sim_end:
            continue
        key = (kind, oid)
        if te - last.get(key, -9) < 0.08:
            continue
        win = int(te * 16)
        if win_count.get(win, 0) >= 2:
            continue
        pan = min(0.9, max(0.1, x / W))
        if kind == "peg":
            win_count[win] = win_count.get(win, 0) + 1
            last[key] = te
            mallet(buf, te, pent_hz(root, oid), 0.05 + 0.11 * min(1.0, speed / 900.0), pan)
        elif kind == "bb" and speed > 250:
            win_count[win] = win_count.get(win, 0) + 1
            last[key] = te
            bloop(buf, te, 330, 260, 0.07, 0.04, pan)

    # resultado: arpegio mayor ascendente
    for i, ratio in enumerate((1.0, 1.25, 1.5, 2.0)):
        mallet(buf, tl.t_first + 0.05 + i * 0.11, base * ratio, 0.16)

    buf = buf[: int(total * SR) + SR // 2]
    buf = reverb(buf, seed)
    buf = np.tanh(buf * 1.4) / np.tanh(1.4)                  # limitador suave
    buf = buf[: int(total * SR)]
    fade = np.minimum(1.0, np.maximum(0.0, total - tt[: len(buf)]) / 0.5)
    buf *= fade[:, None]
    peak = np.max(np.abs(buf)) or 1.0
    buf = buf / peak * 0.72
    pcm = (np.clip(buf, -1, 1) * 32767).astype(np.int16)
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(pcm.tobytes())


# --------------------------------------------------------------------------
# PIPELINE
# --------------------------------------------------------------------------
def pick_best_seed(base_seed, n_cand, course=0, palette=0, verbose=True, min_pool=14, max_cand=500):
    """Simula pistas hasta tener al menos `min_pool` candidatas validas donde gana la
    posicion de salida sorteada, y elige la mas tensa. Asi la posicion inicial de las bolas
    NO sirve como pista para adivinar (cada video es igualmente una simulacion real)."""
    target_slot = random.Random(base_seed * 7919 + 13).randrange(3)
    cands, c = [], 0
    while c < max_cand:
        seed = base_seed * 1000 + c
        c += 1
        sim = simulate(seed, course, palette)
        if sim is None:
            continue
        sc, info = tension_score(sim)
        slot = min(range(sim["n"]), key=lambda i: sim["fin"][i])
        cands.append((sc, slot, sim, info))
        pool = [x for x in cands if x[1] == target_slot]
        if c >= n_cand and len(pool) >= min_pool:
            break
    if not cands:
        return None
    pool = [x for x in cands if x[1] == target_slot] or cands
    best = max(pool, key=lambda x: x[0])
    if verbose:
        print(f"  {c} pistas simuladas, {len(cands)} validas; posicion ganadora sorteada={target_slot}; "
              f"pool={len(pool)}")
    return best[0], best[2], best[3]


def make_reel(base_seed, lang, out_dir, n_cand, palette=None):
    course = make_course(base_seed)
    palette = (base_seed * 7 + 1) % len(PALETTES) if palette is None else palette
    if shutil.which("ffmpeg") is None:
        sys.exit("ERROR: no encuentro FFmpeg en el PATH. Instalalo (gratis) y reintenta.")
    os.makedirs(out_dir, exist_ok=True)
    tx = TEXT[lang]
    t0 = time.time()
    print(f"[1/5] Generando y puntuando {n_cand} experimentos candidatos...")
    best = pick_best_seed(base_seed, n_cand, course, palette)
    if best is None:
        sys.exit("ERROR: ningun candidato termino la carrera. Proba otra semilla.")
    sc, sim, info = best
    seed = sim["seed"]
    print(f"      elegido seed={seed}  score={sc:.2f}  {info}")

    n = sim["n"]
    letters = LETTERS[:n]
    ball_letters = [letters[sim['ids'][i]] for i in range(n)]
    winner_i = int(np.argmin(sim["fin"]))
    fins_sorted = sorted(sim["fin"])
    margin = fins_sorted[1] - fins_sorted[0]
    tl = Timeline(sim)

    print("[2/5] Sintetizando audio original...")
    stem = f"hunch_{base_seed:04d}"
    wav = os.path.join(out_dir, stem + ".wav")
    synth_audio(sim, tl, wav, seed=base_seed)

    print("[3/5] Preparando escena...")
    sim["cams"] = compute_cams(sim)
    prepare_decor(sim, base_seed)
    make_extras()
    static = build_static(sim)
    sprites = [make_ball_sprite(BALL_COLORS[i], letters[i]) for i in range(n)]
    first = render_frame(0.0, sim, tl, static, sprites, tx, ball_letters, winner_i, margin)
    cover = os.path.join(out_dir, stem + "_cover.jpg")
    first.save(cover, quality=92)

    print(f"[4/5] Renderizando {tl.n_frames} frames ({tl.t_total:.1f} s) y codificando...")
    mp4 = os.path.join(out_dir, stem + ".mp4")
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
        "-i", wav,
        "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p",
        "-profile:v", "high", "-r", str(FPS), "-g", str(FPS * 2),
        "-c:a", "aac", "-b:a", "128k", "-ar", "48000", "-ac", "2",
        "-t", f"{tl.t_total:.3f}", "-movflags", "+faststart", mp4,
    ]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    loop_start = tl.t_total - tl.loop_len
    for f in range(tl.n_frames):
        t = f / FPS
        frame = render_frame(t, sim, tl, static, sprites, tx, ball_letters, winner_i, margin)
        if t >= loop_start:           # fundido hacia el primer frame -> loop limpio
            a = (t - loop_start) / tl.loop_len
            frame = Image.blend(frame, first, min(1.0, a))
        proc.stdin.write(frame.tobytes())
        if f % 90 == 0:
            print(f"      frame {f}/{tl.n_frames}")
    proc.stdin.close()
    rc = proc.wait()
    if rc != 0:
        sys.exit("ERROR: FFmpeg fallo al codificar.")
    os.remove(wav)

    print("[5/5] Metadatos...")
    opts = ", ".join(letters[:-1]) + " or " + letters[-1] if lang == "en" else \
        ", ".join(letters[:-1]) + " o " + letters[-1]
    caption = tx["caption"].format(opts=opts) + "\n\n" + tx["tags"]
    meta = {
        "version": "0.1", "base_seed": base_seed, "seed": seed, "lang": lang,
        "experiment": "ball_race_prediction", "course": course, "palette": palette, "n_balls": n,
        "winner": ball_letters[winner_i], "finish_times_s": [round(x, 3) for x in sim["fin"]],
        "win_margin_s": round(margin, 3), "tension_score": round(sc, 3), "tension": info,
        "duration_s": round(tl.t_total, 2), "resolution": f"{W}x{H}", "fps": FPS,
        "caption": caption, "ai_generated": False,
        "files": {"video": os.path.basename(mp4), "cover": os.path.basename(cover)},
    }
    with open(os.path.join(out_dir, stem + ".json"), "w", encoding="utf-8") as fh:
        json.dump(meta, fh, ensure_ascii=False, indent=2)
    print(f"\nLISTO en {time.time() - t0:.0f} s  ->  {mp4}")
    print(f"Ganador real: {ball_letters[winner_i]}  (margen {margin:.2f} s)")
    return mp4


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Hunch Lab V0.1 - generador de un Reel")
    ap.add_argument("--seed", type=int, default=1, help="semilla base (cambia el experimento)")
    ap.add_argument("--lang", choices=["en", "es"], default="en")
    ap.add_argument("--out", default="out")
    ap.add_argument("--palette", type=int, default=None, help="0-3: paleta de colores")
    ap.add_argument("--candidates", type=int, default=24,
                    help="cuantos experimentos probar antes de elegir el mas tenso")
    a = ap.parse_args()
    make_reel(a.seed, a.lang, a.out, a.candidates, a.palette)
