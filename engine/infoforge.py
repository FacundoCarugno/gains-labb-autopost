#!/usr/bin/env python3
"""infoforge.py -- Gains Lab: Reels informativos de fitness (voz + mascota + subtitulos EN/ES).
Todo se genera por codigo: Pillow + numpy + FFmpeg + Kokoro TTS local (Apache-2.0). Sin APIs ni musica de terceros.
"""
import argparse, hashlib, json, math, os, subprocess, sys, time, wave
import numpy as np
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from reelforge import W, H, FPS, SR, get_font, fit_font, mix, mallet, bloop, reverb, _pan
from mascot import draw_mascot, POSES, lerp_pose, blink_factor

CREAM = (255, 244, 230); ORANGE = (255, 122, 24); LIME = (166, 236, 70); CYAN = (64, 214, 255)
YELLOW = (255, 214, 10); BLUE = (90, 140, 255); MUTED = (178, 168, 172); CARD = (36, 27, 32)
BGC = (17, 12, 13); HILITE = (255, 214, 10); SUB_OTHER = (150, 215, 255)
LEAD, GAP = 0.45, 0.25
BRAND = "GAINS LAB"
Q = 0      # nivel de calidad del video (0..7), acumulativo
DAY = 0


# ------------------------------------------------------------------ voz
class Voice:
    def __init__(self, model_dir, sid=3, speed=1.05, cache_dir="cache"):
        import sherpa_onnx as so
        m = model_dir
        kc = so.OfflineTtsKokoroModelConfig(
            model=f"{m}/model.onnx", voices=f"{m}/voices.bin", tokens=f"{m}/tokens.txt",
            data_dir=f"{m}/espeak-ng-data", dict_dir=f"{m}/dict",
            lexicon=f"{m}/lexicon-us-en.txt,{m}/lexicon-zh.txt")
        cfg = so.OfflineTtsConfig(model=so.OfflineTtsModelConfig(kokoro=kc, num_threads=4, provider="cpu"))
        self.tts = so.OfflineTts(cfg)
        self.sid, self.speed, self.cache = sid, speed, cache_dir
        os.makedirs(cache_dir, exist_ok=True)

    def say(self, text):
        key = hashlib.md5(f"en|{self.sid}|{self.speed}|{text}".encode()).hexdigest()
        p = os.path.join(self.cache, key + ".npy")
        if os.path.exists(p):
            return np.load(p)
        a = self.tts.generate(text, sid=self.sid, speed=self.speed)
        x = np.asarray(a.samples, dtype=np.float32)
        n_out = int(len(x) * SR / a.sample_rate)
        x = np.interp(np.linspace(0, len(x) - 1, n_out), np.arange(len(x)), x).astype(np.float32)
        idx = np.where(np.abs(x) > 0.012)[0]
        if len(idx):
            x = x[max(0, idx[0] - int(0.04 * SR)): idx[-1] + int(0.06 * SR)]
        rms = float(np.sqrt(np.mean(x ** 2)) + 1e-9)
        x = x * (0.11 / rms)
        x = np.tanh(x * 1.2) / 1.2
        np.save(p, x)
        return x


# ------------------------------------------------------------------ utilidades de dibujo
def ease_out(x):
    x = max(0.0, min(1.0, x)); return 1 - (1 - x) ** 3

def pop(x):
    x = max(0.0, min(1.0, x))
    return 1 + 0.12 * math.sin(x * math.pi) * (1 - x) * 3 if x < 1 else 1.0

def txt(d, xy, s, font, fill=CREAM, stroke=0, sf=(8, 6, 8), anchor="mm"):
    d.text(xy, s, font=font, fill=fill, anchor=anchor, stroke_width=stroke, stroke_fill=sf)

def wrap(d, s, font, maxw):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def card(d, box, fill=CARD, r=40):
    d.rounded_rectangle(box, radius=r, fill=fill)

_RING = {}
def ring_patch(frac, color, size=520, width=56):
    key = (int(frac * 160), color)
    if key in _RING: return _RING[key]
    SS = 2; S = size * SS
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); g = ImageDraw.Draw(im)
    pad = width * SS // 2 + 4
    g.ellipse([pad, pad, S - pad, S - pad], outline=(60, 48, 54, 255), width=width * SS)
    if frac > 0.003:
        g.arc([pad, pad, S - pad, S - pad], -90, -90 + 360 * frac, fill=color + (255,), width=width * SS)
        a = math.radians(-90 + 360 * frac); rr = (S - 2 * pad) / 2
        for ang in (math.radians(-90), a):
            cx, cy = S / 2 + rr * math.cos(ang), S / 2 + rr * math.sin(ang)
            g.ellipse([cx - width * SS / 2, cy - width * SS / 2, cx + width * SS / 2, cy + width * SS / 2], fill=color + (255,))
    im = im.resize((size, size), Image.LANCZOS)
    _RING[key] = im
    return im


def back(x):
    x = max(0.0, min(1.0, x)); c1 = 1.70158; c3 = c1 + 1
    return 1 + c3 * (x - 1) ** 3 + c1 * (x - 1) ** 2

_GLOW = {}
def glow_sprite(color, size):
    key = (color, size)
    if key not in _GLOW:
        yy, xx = np.mgrid[0:size, 0:size]
        r = np.hypot(xx - size / 2, yy - size / 2) / (size / 2)
        a = np.clip(1 - r, 0, 1) ** 2 * 64
        arr = np.zeros((size, size, 4), np.uint8)
        arr[..., 0], arr[..., 1], arr[..., 2], arr[..., 3] = color[0], color[1], color[2], a.astype(np.uint8)
        _GLOW[key] = Image.fromarray(arr, "RGBA")
    return _GLOW[key]

BLOBS = [((255, 122, 24), 900, 420, 700, 0.35, 0.22, 0.0), ((64, 160, 255), 800, 450, 650, 0.28, 0.31, 2.0),
         ((166, 236, 70), 700, 380, 720, 0.40, 0.25, 4.0)]
_rs = np.random.default_rng(11)
SPARKS = [(_rs.uniform(30, W - 30), _rs.uniform(0, H), _rs.uniform(0.4, 1.2), _rs.uniform(0, 6), _rs.uniform(8, 16)) for _ in range(18)]

def living_bg(img, d, tt):
    for (c, sz, ax, ay, fx, fy, ph) in BLOBS:
        x = 540 + ax * math.sin(tt * fx + ph) - sz / 2; y = 960 + ay * math.sin(tt * fy + ph * 1.7) - sz / 2
        sp = glow_sprite(c, sz); img.paste(sp, (int(x), int(y)), sp)
    for (x, y, sp, ph, sz) in SPARKS:
        yy = (y - tt * 55 * sp) % H; tw = 0.5 + 0.5 * math.sin(tt * 3 + ph); r = sz * (0.35 + 0.65 * tw)
        col = mix((70, 54, 58), CREAM, tw)
        d.line([(x - r, yy), (x + r, yy)], fill=col, width=3); d.line([(x, yy - r), (x, yy + r)], fill=col, width=3)

_ICON = {}
def icon_patch(name, size, color):
    key = (name, size, color)
    if key in _ICON: return _ICON[key]
    SS = 3; S = size * SS; u = S / 100.0
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); g = ImageDraw.Draw(im); c = color + (255,); T = (0, 0, 0, 0)
    P = lambda *pts: [(x * u, y * u) for x, y in pts]
    if name == "dumbbell":
        g.rounded_rectangle([28 * u, 45 * u, 72 * u, 55 * u], radius=3 * u, fill=c)
        for x0, hh in ((10, 24), (22, 17), (68, 17), (78, 24)):
            g.rounded_rectangle([x0 * u, (50 - hh) * u, (x0 + 11) * u, (50 + hh) * u], radius=4 * u, fill=c)
    elif name == "moon":
        g.ellipse([14 * u, 12 * u, 86 * u, 84 * u], fill=c); g.ellipse([36 * u, 4 * u, 100 * u, 68 * u], fill=T)
    elif name == "flame":
        g.polygon(P((50, 5), (68, 34), (82, 60), (70, 88), (50, 96), (30, 88), (18, 60), (32, 38), (42, 52)), fill=c)
        g.polygon(P((50, 56), (62, 74), (50, 90), (38, 74)), fill=T)
    elif name == "clock":
        g.ellipse([8 * u, 8 * u, 92 * u, 92 * u], outline=c, width=int(9 * u))
        g.line(P((50, 50), (50, 24)), fill=c, width=int(9 * u)); g.line(P((50, 50), (68, 60)), fill=c, width=int(9 * u))
    elif name == "heart":
        g.ellipse([12 * u, 16 * u, 54 * u, 58 * u], fill=c); g.ellipse([46 * u, 16 * u, 88 * u, 58 * u], fill=c)
        g.polygon(P((15, 45), (85, 45), (50, 90)), fill=c)
    elif name == "bolt":
        g.polygon(P((60, 4), (20, 56), (46, 56), (36, 96), (80, 38), (54, 38)), fill=c)
    elif name == "check":
        g.line(P((20, 52), (42, 74), (82, 28)), fill=c, width=int(13 * u), joint="curve")
    elif name == "cross":
        g.line(P((24, 24), (76, 76)), fill=c, width=int(13 * u)); g.line(P((76, 24), (24, 76)), fill=c, width=int(13 * u))
    elif name == "target":
        g.ellipse([8 * u, 8 * u, 92 * u, 92 * u], outline=c, width=int(8 * u)); g.ellipse([28 * u, 28 * u, 72 * u, 72 * u], outline=c, width=int(8 * u))
        g.ellipse([43 * u, 43 * u, 57 * u, 57 * u], fill=c)
    elif name == "calendar":
        g.rounded_rectangle([12 * u, 20 * u, 88 * u, 90 * u], radius=9 * u, outline=c, width=int(8 * u))
        g.rectangle([12 * u, 20 * u, 88 * u, 40 * u], fill=c)
        for x0 in (30, 66): g.line(P((x0, 8), (x0, 28)), fill=c, width=int(8 * u))
        for (x0, y0) in ((28, 52), (46, 52), (64, 52), (28, 68), (46, 68)): g.rectangle([x0 * u, y0 * u, (x0 + 10) * u, (y0 + 9) * u], fill=c)
    elif name == "walk":
        g.ellipse([40 * u, 6 * u, 60 * u, 26 * u], fill=c)
        for a, b in (((50, 30), (50, 60)), ((50, 60), (34, 92)), ((50, 60), (66, 90)), ((50, 38), (32, 56)), ((50, 38), (68, 52))):
            g.line(P(a, b), fill=c, width=int(9 * u))
    elif name == "list":
        for i in range(3):
            y = 24 + i * 26
            g.ellipse([12 * u, (y - 6) * u, 24 * u, (y + 6) * u], fill=c); g.rounded_rectangle([34 * u, (y - 5) * u, 90 * u, (y + 5) * u], radius=4 * u, fill=c)
    elif name == "flask":
        g.polygon(P((38, 8), (62, 8), (62, 40), (88, 90), (12, 90), (38, 40)), fill=c); g.polygon(P((30, 70), (70, 70), (78, 84), (22, 84)), fill=T)
    im = im.resize((size, size), Image.LANCZOS); _ICON[key] = im
    return im

def put_icon(img, name, cx, cy, size, color, scale=1.0):
    sz = max(8, int(size * scale)); ip = icon_patch(name, int(size), color)
    if sz != size: ip = ip.resize((sz, sz), Image.LANCZOS)
    img.paste(ip, (int(cx - sz / 2), int(cy - sz / 2)), ip)

def tracker(d, day):
    start = 1 if day <= 12 else day - 6
    for i in range(12):
        n = start + i; x = 210 + i * 60; y = 190
        if n < day: d.ellipse([x - 11, y - 11, x + 11, y + 11], fill=LIME)
        elif n == day:
            d.ellipse([x - 19, y - 19, x + 19, y + 19], fill=ORANGE, outline=CREAM, width=3)
            txt(d, (x, y), str(day), get_font(20 if day < 100 else 15), (20, 14, 12))
        else: d.ellipse([x - 8, y - 8, x + 8, y + 8], fill=(66, 54, 60))

def confetti(d, lt, cx, cy, t0=1.3, dur=1.5):
    x = lt - t0
    if x < 0 or x > dur: return
    r = np.random.default_rng(7)
    for i in range(46):
        ang = r.uniform(-math.pi * 0.95, -math.pi * 0.05); v = r.uniform(380, 900); col = [ORANGE, LIME, CYAN, YELLOW, CREAM][i % 5]; sz = r.uniform(8, 16)
        px = cx + math.cos(ang) * v * x; py = cy + math.sin(ang) * v * x + 1000 * x * x
        if i % 2: d.ellipse([px - sz / 2, py - sz / 2, px + sz / 2, py + sz / 2], fill=col)
        else: d.rectangle([px - sz / 2, py - sz / 3, px + sz / 2, py + sz / 3], fill=col)

def zoom_img(img, z):
    if z <= 1.0005: return img
    w2, h2 = W / z, H / z; x0 = (W - w2) / 2; y0 = 900 - h2 * 900 / H
    return img.resize((W, H), Image.BILINEAR, box=(x0, y0, x0 + w2, y0 + h2))

_VIG = None
def vignette(img):
    global _VIG
    if _VIG is None:
        yy, xx = np.mgrid[0:H, 0:W]; r = np.hypot((xx - W / 2) / (W / 2), (yy - H / 2) / (H / 2))
        _VIG = Image.fromarray((np.clip((r - 0.62) / 0.75, 0, 1) ** 1.6 * 170).astype(np.uint8), "L")
    img.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), _VIG)

def wipe(d, lt):
    if lt >= 0.4: return
    p = ease_out(lt / 0.4); x = -420 + (W + 700) * p
    d.polygon([(x + 160, 0), (x + 420, 0), (x + 260, H), (x, H)], fill=ORANGE)
    d.polygon([(x + 110, 0), (x + 150, 0), (x - 10, H), (x - 50, H)], fill=CREAM)

def anim_state(kind, tt):
    k = (math.sin(tt * 2 * math.pi * 1.5) + 1) / 2
    if kind == "jack":
        return lerp_pose(POSES["idle"], POSES["cheer"], k), dict(spread=int(70 * k), dy=-abs(math.sin(tt * 2 * math.pi * 1.5)) * 30, squash=1.0)
    if kind == "squat":
        return POSES["present"], dict(spread=int(30 * k), dy=0, squash=1 - 0.17 * k)
    if kind == "circles":
        a = (tt * 300) % 360
        return (a, a, a, a), dict(spread=0, dy=0, squash=1.0)
    return None, {}


# ------------------------------------------------------------------ escenas
def scene_hook(img, d, sc, lt, tl, t):
    e = ease_out(lt / 0.5)
    txt(d, (540, 270 + (1 - e) * 40), "DAY", get_font(76), ORANGE, 4)
    n = pop(lt / 0.6); f = get_font(int(300 * n))
    txt(d, (540, 420), str(sc["day"]), f, CREAM, 10)
    if Q >= 3 and sc.get("icon"):
        put_icon(img, sc["icon"], 850, 420 + math.sin(lt * 3) * 10, 190, ORANGE, back((lt - 0.3) / 0.5))
    f = fit_font(d, sc["teach_en"], 900, 66)
    w = d.textlength(sc["teach_en"], font=f) + 90
    d.rounded_rectangle([540 - w / 2, 560, 540 + w / 2, 650], radius=45, fill=LIME)
    txt(d, (540, 606), sc["teach_en"], f, (22, 30, 12))
    txt(d, (540, 695), sc["teach_es"], fit_font(d, sc["teach_es"], 900, 42), MUTED)
    if Q >= 5:
        wi = 0; nw = sum(len(l.split()) for l in sc["title"])
        for i, ln in enumerate(sc["title"]):
            f = fit_font(d, ln, 960, 88); words = ln.split(); sp = d.textlength(" ", font=f)
            ws = [d.textlength(w_, font=f) for w_ in words]; x = 540 - (sum(ws) + sp * (len(words) - 1)) / 2
            for k, w_ in enumerate(words):
                tw0 = 0.5 + wi * 0.16; e2 = back((lt - tw0) / 0.4)
                if lt >= tw0:
                    f2 = get_font(max(10, int(f.size * max(0.25, e2))))
                    txt(d, (x + ws[k] / 2, 790 + i * 95), w_, f2, ORANGE if wi == nw - 1 else CREAM, 7)
                x += ws[k] + sp; wi += 1
    else:
        for i, ln in enumerate(sc["title"]):
            y = 790 + i * 95 + (1 - ease_out((lt - 0.5 - i * 0.15) / 0.5)) * 50
            txt(d, (540, y), ln, fit_font(d, ln, 960, 88), CREAM, 7)

def scene_stat(img, d, sc, lt, tl, t):
    e = ease_out(lt / 0.5); oy = (1 - e) * 60
    card(d, (60, 250 + oy, 1020, 1075 + oy))
    txt(d, (540, 340 + oy), sc["head"], fit_font(d, sc["head"], 860, 56), ORANGE)
    fr = sc["ring"] * ease_out((lt - 0.4) / 1.4)
    img.paste(ring_patch(fr, CYAN), (280, 410 + int(oy)), ring_patch(fr, CYAN))
    val = sc["value"]
    if Q >= 4 and sc.get("count"):
        end, fmt = sc["count"]; val = fmt.format(end * ease_out((lt - 0.4) / 1.3))
    txt(d, (540, 670 + oy), val, get_font(int(sc.get("vsize", 190) * pop((lt - 0.4) / 0.6))), CREAM, 6)
    if Q >= 3 and sc.get("icon"):
        put_icon(img, sc["icon"], 915, 520 + oy + math.sin(lt * 3) * 6, 120, ORANGE, back((lt - 0.2) / 0.5))
    for i, s_ in enumerate(sc["label"]):
        txt(d, (540, 985 + oy + i * 52), s_, get_font(46), CYAN if i == 0 else MUTED)
    if Q >= 6: confetti(d, lt, 540, 670)

def scene_vs(img, d, sc, lt, tl, t):
    e = ease_out(lt / 0.5); oy = (1 - e) * 60
    txt(d, (540, 295 + oy), sc["head"], fit_font(d, sc["head"], 900, 64), ORANGE, 3)
    if sc.get("sub"): txt(d, (540, 362 + oy), sc["sub"], fit_font(d, sc["sub"], 900, 34), MUTED)
    for i, row in enumerate(sc["rows"]):
        t0 = sc["_lines"][i + 1]["t0"]; g = ease_out((t - t0 + 0.05) / 0.5) if t >= t0 - 0.05 else 0.0
        if g <= 0: continue
        y = 430 + i * 330 + (1 - back(g)) * 60
        card(d, (60, y, 1020, y + 300))
        if row.get("win"): d.rounded_rectangle([60, y, 1020, y + 300], radius=40, outline=LIME, width=6)
        txt(d, (110, y + 75), row["title"], fit_font(d, row["title"], 470, 46), CREAM, anchor="lm")
        txt(d, (110, y + 140), row["sub"], fit_font(d, row["sub"], 470, 32), MUTED, anchor="lm")
        txt(d, (110, y + 210), row["es"], fit_font(d, row["es"], 470, 30), SUB_OTHER, anchor="lm")
        v = row["val"] * ease_out((t - t0) / 1.0)
        txt(d, (985, y + 150), row["fmt"].format(v), get_font(112), LIME if row.get("win") else CREAM, 6, anchor="rm")

def scene_recap(img, d, sc, lt, tl, t):
    txt(d, (540, 290), sc["head"], fit_font(d, sc["head"], 900, 66), ORANGE, 3)
    for i, (n, name) in enumerate(sc["items"]):
        c, r = i % 3, i // 3
        tp = 0.9 + i * 0.62
        e = back((lt - tp) / 0.45)
        if lt < tp: continue
        w_, h_ = 300 * min(1.0, e), 168 * min(1.0, e)
        cx_, cy_ = 60 + c * 330 + 150, 360 + r * 192 + 84
        d.rounded_rectangle([cx_ - w_ / 2, cy_ - h_ / 2, cx_ + w_ / 2, cy_ + h_ / 2], radius=30, fill=CARD, outline=LIME if e >= 1 else None, width=3)
        if e > 0.9:
            txt(d, (cx_ - 98, cy_ - 8), str(n), get_font(62), ORANGE, 3, anchor="mm")
            txt(d, (cx_ + 36, cy_ - 8), name, fit_font(d, name, 150, 32, 22), CREAM, anchor="mm")
            put_icon(img, "check", cx_ + 112, cy_ - 52, 34, LIME)

def scene_bars(img, d, sc, lt, tl, t):
    e = ease_out(lt / 0.5); oy = (1 - e) * 60
    card(d, (60, 250 + oy, 1020, 1075 + oy))
    txt(d, (540, 340 + oy), sc["head"], fit_font(d, sc["head"], 860, 60), ORANGE)
    txt(d, (540, 405 + oy), sc["sub"], fit_font(d, sc["sub"], 860, 38), MUTED)
    mx = max(v for _, v in sc["rows"]); cols = [BLUE, CYAN, LIME, YELLOW]
    for i, (lab, val) in enumerate(sc["rows"]):
        y = 520 + i * 175 + oy
        txt(d, (110, y), lab, get_font(42), CREAM, anchor="lm")
        t0 = sc["_lines"][i + 1]["t0"]
        g = ease_out((t - t0) / 0.9) if t >= t0 else 0.0
        d.rounded_rectangle([110, y + 38, 110 + 820, y + 100], radius=31, fill=(58, 46, 52))
        bw = 62 + (820 - 62) * (val / mx) * g
        if g > 0:
            d.rounded_rectangle([110, y + 38, 110 + bw, y + 100], radius=31, fill=cols[i])
            txt(d, (110 + bw - 24, y + 70), f"~{sc.get('fmt', '{:.1f}').format(val * g)}{sc['unit']}", get_font(38), (20, 18, 20), anchor="rm")
    txt(d, (540, 1040 + oy), sc["footer"], get_font(30), MUTED)

def scene_tips(img, d, sc, lt, tl, t):
    txt(d, (540, 300), sc["head"], fit_font(d, sc["head"], 900, 70), ORANGE, 3)
    icons = Q >= 3 and sc.get("icons")
    mw = 680 if icons else 770
    for i, (en, es) in enumerate(sc["items"]):
        t0 = sc["_lines"][i]["t0"]
        e0 = ease_out((t - t0 + 0.05) / 0.45) if t >= t0 - 0.05 else 0.0
        if e0 <= 0: continue
        e = back((t - t0 + 0.05) / 0.5) if Q >= 5 else e0
        y0 = 360 + i * 245 + (1 - e) * 70
        card(d, (60, y0, 1020, y0 + 218), r=36)
        d.ellipse([90, y0 + 62, 185, y0 + 157], fill=[ORANGE, CYAN, LIME][i])
        txt(d, (137, y0 + 110), str(i + 1), get_font(62), (20, 16, 18))
        f = get_font(46)
        while len(wrap(d, en, f, mw)) > 2 and f.size > 30: f = get_font(f.size - 2)
        ls = wrap(d, en, f, mw)
        for j, l in enumerate(ls):
            txt(d, (215, y0 + 42 + j * (f.size + 8)), l, f, CREAM, anchor="lm")
        f2 = get_font(30 if not icons else 27)
        es_l = wrap(d, es, f2, mw)
        ey = y0 + 42 + len(ls) * (f.size + 8) + 10
        for j, l in enumerate(es_l[:2]):
            txt(d, (215, ey + j * 34), l, f2, SUB_OTHER, anchor="lm")
        if icons:
            put_icon(img, sc["icons"][i], 955, y0 + 109, 84, [ORANGE, CYAN, LIME][i])

def scene_cta(img, d, sc, lt, tl, t):
    e = ease_out(lt / 0.5)
    txt(d, (540, 360), "SAVE THIS", get_font(int(150 * pop(lt / 0.6))), CREAM, 8)
    txt(d, (540, 520), "& FOLLOW", get_font(120), ORANGE, 6)
    f = get_font(60); w = d.textlength(tl["handle"], font=f) + 80
    d.rounded_rectangle([540 - w / 2, 610, 540 + w / 2, 700], radius=45, fill=CARD)
    txt(d, (540, 655), tl["handle"], f, CYAN)
    s_ = sc["next_en"]; f = fit_font(d, s_, 880, 56); w = d.textlength(s_, font=f) + 90
    d.rounded_rectangle([540 - w / 2, 750, 540 + w / 2, 840], radius=45, fill=LIME)
    txt(d, (540, 795), s_, f, (22, 30, 12))
    txt(d, (540, 885), sc["next_es"], get_font(40), MUTED)

SCENES = {"hook": scene_hook, "stat": scene_stat, "bars": scene_bars, "tips": scene_tips, "cta": scene_cta, "vs": scene_vs, "recap": scene_recap}
MASCOT = {"hook": ("wave", 1225, 0.98, 540), "stat": ("point", 1250, 0.56, 170), "bars": ("present", 1250, 0.56, 170),
          "tips": ("cheer", 1250, 0.56, 170), "cta": ("flex", 1190, 0.88, 540), "vs": ("present", 1250, 0.56, 170), "recap": ("cheer", 1295, 0.5, 540)}


# ------------------------------------------------------------------ subtitulos
def active_sub(sc_list, t):
    for sc in sc_list:
        for ln in sc["_lines"]:
            if ln["t0"] <= t < ln["t1"] + 0.18:
                p = min(0.999, max(0.0, (t - ln["t0"]) / max(1e-3, ln["t1"] - ln["t0"])))
                return ln, p
    return None, 0

def pick_chunk(chunks, p):
    tot = sum(len(c) for c in chunks); acc = 0
    for i, c in enumerate(chunks):
        lo, hi = acc / tot, (acc + len(c)) / tot
        if p < hi or i == len(chunks) - 1:
            return c, min(1.0, max(0.0, (p - lo) / max(1e-6, hi - lo))), i
        acc += len(c)

def draw_subs(img, d, sc_list, t):
    ln, p = active_sub(sc_list, t)
    if not ln: return
    en, pe, ie = pick_chunk(ln["sub_en"], p)
    es = ln["sub_es"][ie] if (Q >= 1 and len(ln["sub_es"]) == len(ln["sub_en"])) else pick_chunk(ln["sub_es"], p)[0]
    box = (40, 1440, 1040, 1760)
    reg = img.crop(box); dark = Image.new("RGB", reg.size, (8, 6, 8))
    img.paste(Image.blend(reg, dark, 0.66), box)
    f = fit_font(d, en, 940, 66, 40)
    words = en.split(); tw = sum(d.textlength(w, font=f) for w in words) + d.textlength(" ", font=f) * (len(words) - 1)
    x = 540 - tw / 2; hi = min(len(words) - 1, int(pe * len(words)))
    for i, w in enumerate(words):
        txt(d, (x, 1555), w, f, HILITE if i == hi else CREAM, 4, anchor="lm")
        x += d.textlength(w + " ", font=f)
    fe = fit_font(d, es, 940, 44, 26)
    txt(d, (540, 1670), es, fe, SUB_OTHER, 3)


# ------------------------------------------------------------------ audio
def synth_audio(scenes, total, voice_tr, path, seed=3, day=2):
    N = int(total * SR) + SR
    mus = np.zeros((N, 2)); sfx = np.zeros((N, 2)); rng = np.random.default_rng(seed)
    bpm = 100; beat = 60 / bpm
    MA, MI = [0, 4, 7, 12], [0, 3, 7, 12]
    prog = [(130.81, MA), (110.0, MI), (87.31, MA), (98.0, [0, 4, 7, 11])]
    if Q >= 1:
        bpm = 96 + (day * 3) % 14; beat = 60 / bpm
        prog = [[(110.0, MI), (87.31, MA), (130.81, MA), (98.0, MA)], [(98.0, MA), (130.81, MA), (110.0, MI), (87.31, MA)],
                [(87.31, MA), (98.0, MA), (110.0, MI), (130.81, MA)], [(130.81, MA), (98.0, MA), (110.0, MI), (87.31, MA)]][day % 4]
    nb = int(total / beat) + 2
    for b in range(nb):
        t0 = b * beat
        root, ch = prog[(b // 4) % 4]
        i0 = int(t0 * SR); n = int(0.22 * SR)
        if i0 + n < N:
            tt = np.arange(n) / SR
            f = 45 + 80 * np.exp(-tt / 0.03)
            k = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-tt / 0.09) * 0.55
            _pan(mus, i0, k, 0.5)
        h0 = int((t0 + beat / 2) * SR); n = int(0.05 * SR)
        if h0 + n < N:
            nz = np.diff(rng.standard_normal(n + 1)) * np.exp(-np.arange(n) / (0.012 * SR)) * 0.10
            _pan(mus, h0, nz, 0.62)
        if b % 2 == 0:
            tt = np.arange(int(0.8 * SR)) / SR; fr = root / 2
            if int(t0 * SR) + len(tt) < N:
                _pan(mus, int(t0 * SR), (np.sin(2 * np.pi * fr * tt) + 0.3 * np.sin(4 * np.pi * fr * tt)) * np.exp(-tt / 0.45) * 0.30, 0.5)
        if Q >= 3 and b % 2 == 1:
            hn = int(0.09 * SR)
            if int(t0 * SR) + hn < N:
                cl = np.diff(rng.standard_normal(hn + 1)) * np.exp(-np.arange(hn) / (0.03 * SR)) * 0.16
                _pan(mus, int(t0 * SR), cl, 0.5)
        if Q >= 6 and b % 4 == 0:
            ln_ = int(4 * beat * SR)
            if int(t0 * SR) + ln_ < N:
                tt = np.arange(ln_) / SR; env = np.sin(np.pi * tt / (4 * beat)) ** 2
                pad = sum(np.sin(2 * np.pi * root * 2 * 2 ** (st / 12) * tt) for st in ch[:3]) * 0.03 * env
                _pan(mus, int(t0 * SR), pad, 0.5)
        for e8 in range(2):
            tn = t0 + e8 * beat / 2
            st = ch[(b * 2 + e8) % len(ch)]
            mallet(mus, tn, root * 2 * 2 ** (st / 12), 0.055, 0.35 + 0.3 * ((b * 2 + e8) % 3) / 2)
    mus = reverb(mus, seed, wet=0.28, rt=1.1)
    # ducking con la voz
    env = np.abs(voice_tr); k = int(0.08 * SR)
    env = np.convolve(env, np.ones(k) / k, mode="same"); env = np.minimum(1.0, env / 0.12)
    env = np.convolve(env, np.ones(int(0.25 * SR)) / int(0.25 * SR), mode="same")
    duck = 1 - 0.62 * env
    mus *= np.pad(duck, (0, N - len(duck)))[:N, None]
    # fade final
    fo = int(1.2 * SR); mus[int(total * SR) - fo:int(total * SR)] *= np.linspace(1, 0, fo)[:, None]
    # sfx: whoosh en cada escena + campanita en tips/barras
    for sc in scenes:
        i0 = int(sc["t0"] * SR); n = int(0.4 * SR)
        if i0 + n < N:
            tt = np.arange(n) / SR
            nz = rng.standard_normal(n); nz = np.convolve(nz, np.ones(24) / 24, mode="same")
            w = nz * np.sin(np.pi * tt / 0.4) ** 2 * 0.20
            _pan(sfx, i0, w, 0.5)
        if Q >= 5 and sc["type"] == "hook":
            for wi in range(sum(len(l.split()) for l in sc["title"])):
                mallet(sfx, sc["t0"] + 0.5 + wi * 0.16, 520 * 2 ** (wi / 5), 0.14, 0.5)
        if sc["type"] in ("tips", "bars", "vs"):
            for j, ln in enumerate(sc["_lines"]):
                if (sc["type"] == "tips") or j > 0:
                    mallet(sfx, ln["t0"], 880 * 2 ** (j / 6), 0.12, 0.5)
    out = mus * 0.9 + sfx
    v = np.zeros((N, 2)); v[:len(voice_tr), 0] = voice_tr; v[:len(voice_tr), 1] = voice_tr
    out = out + v * 1.0
    pk = np.max(np.abs(out)) + 1e-9
    out = out / pk * 0.89
    out = out[:int(total * SR)]
    with wave.open(path, "wb") as wf:
        wf.setnchannels(2); wf.setsampwidth(2); wf.setframerate(SR)
        wf.writeframes((np.clip(out, -1, 1) * 32767).astype(np.int16).tobytes())


# ------------------------------------------------------------------ construccion
def L(en, es, sub_en, sub_es):
    return {"en": en, "es": es, "sub_en": sub_en, "sub_es": sub_es}

def reel_volume(handle):
    S = [
        {"type": "hook", "tail": 0.55, "day": 2, "teach_en": "TEACHING YOU: TRAINING VOLUME",
         "teach_es": "Enseñándote: volumen de entrenamiento",
         "title": ["HOW MANY SETS", "PER WEEK TO GROW?"],
         "lines": [L("Day two, teaching you about training volume.", "Día dos, enseñándote sobre el volumen de entrenamiento.",
                     ["Day 2, teaching you","about training volume."], ["Día 2, enseñándote sobre","el volumen de entrenamiento."]),
                   L("How many sets per week do you need to grow muscle?", "¿Cuántas series por semana necesitas para crecer?",
                     ["How many sets per week", "do you need to grow muscle?"], ["¿Cuántas series por semana", "necesitas para crecer?"])]},
        {"type": "stat", "tail": 0.7, "head": "WEEKLY SETS PER MUSCLE", "value": "10+", "ring": 0.5,
         "label": ["hard sets per muscle", "per week, on average"],
         "lines": [L("A review of fifteen studies compared how many weekly sets people did for each muscle.",
                     "Una revisión de quince estudios comparó cuántas series semanales hacía la gente por músculo.",
                     ["A review of 15 studies compared", "weekly sets per muscle."], ["Una revisión de 15 estudios comparó", "las series semanales por músculo."]),
                   L("Ten or more sets per week tended to give the biggest gains.",
                     "Diez o más series por semana tendieron a dar las mayores ganancias.",
                     ["10 or more sets per week", "tended to give the biggest gains."], ["10 o más series por semana", "tendieron a dar las mayores ganancias."])]},
        {"type": "bars", "tail": 0.8, "head": "AVERAGE MUSCLE GAIN", "sub": "by weekly sets per muscle", "unit": "%",
         "rows": [("Under 5 sets", 5.4), ("5 to 9 sets", 6.6), ("10+ sets", 9.8)],
         "footer": "Approximate averages reported in the meta-analysis",
         "lines": [L("Here is the average muscle growth in those studies.", "Este es el crecimiento muscular promedio en esos estudios.",
                     ["Average muscle growth", "in those studies."], ["Crecimiento muscular promedio", "en esos estudios."]),
                   L("Under five sets: about five point four percent.", "Menos de cinco series: cerca de 5,4 %.",
                     ["Under 5 sets: about 5.4%"], ["Menos de 5 series: cerca de 5,4 %"]),
                   L("Five to nine sets: about six point six percent.", "De cinco a nueve series: cerca de 6,6 %.",
                     ["5 to 9 sets: about 6.6%"], ["De 5 a 9 series: cerca de 6,6 %"]),
                   L("Ten or more sets: about nine point eight percent. Almost double.", "Diez o más series: cerca de 9,8 %. Casi el doble.",
                     ["10 or more sets: about 9.8%.", "Almost double."], ["10 o más series: cerca de 9,8 %.", "Casi el doble."])]},
        {"type": "tips", "tail": 0.6, "head": "HOW TO USE THIS",
         "items": [("Start around 10 hard sets per muscle, per week", "Empieza con unas 10 series duras por músculo a la semana"),
                   ("Returns shrink at high volumes. Most studies were in beginners", "Los beneficios se achican con volúmenes altos. Casi todos eran principiantes"),
                   ("Count only hard sets, close to failure", "Cuenta solo series duras, cerca del fallo")],
         "lines": [L("A common starting point is around ten hard sets per muscle each week.", "Un punto de partida común es unas diez series duras por músculo a la semana.",
                     ["A common starting point:", "around 10 hard sets per muscle."], ["Un punto de partida común:", "unas 10 series duras por músculo."]),
                   L("But returns shrink at higher volumes, and most of these studies were in beginners.", "Pero los beneficios se achican con volúmenes altos, y casi todos estos estudios eran en principiantes.",
                     ["But returns shrink at higher volumes,", "and most studies were in beginners."], ["Pero los beneficios se achican con volúmenes altos,", "y casi todos eran en principiantes."]),
                   L("Count only the sets that are hard, close to failure.", "Cuenta solo las series que son duras, cerca del fallo.",
                     ["Count only hard sets,", "close to failure."], ["Cuenta solo series duras,", "cerca del fallo."])]},
        {"type": "cta", "tail": 1.0, "next_en": "DAY 3 TOMORROW: CREATINE", "next_es": "Mañana, día 3: creatina",
         "lines": [L("Save this, and come back tomorrow for day three.", "Guárdalo y vuelve mañana para el día tres.",
                     ["Save this, and come back", "tomorrow for Day 3."], ["Guárdalo y vuelve mañana", "para el Día 3."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 2 teaching you: training volume 💪\n"
           f"How many sets per week do you need to grow muscle? A meta-analysis of 15 studies found that people doing 10+ weekly sets per muscle gained about 9.8% on average, vs ~5.4% for under 5 sets. The category difference was not statistically significant on its own, results mostly came from beginners, and returns shrink at higher volumes.\n\n"
           f"Día 2 enseñándote: volumen de entrenamiento 💪\n"
           f"¿Cuántas series por semana necesitas para crecer? Un metaanálisis de 15 estudios encontró que quienes hacían 10+ series semanales por músculo ganaron ~9,8 % en promedio, frente a ~5,4 % con menos de 5. La diferencia entre categorías no fue estadísticamente significativa por sí sola, casi todos eran principiantes y los beneficios se achican con volúmenes altos.\n\n"
           f"Save this 📌 and follow {handle} — Day 3 tomorrow. / Guárdalo y sigue a {handle}: mañana, Día 3.\n"
           f"Source / Fuente: Schoenfeld, Ogborn & Krieger, J Sports Sci, 2017.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    tags = "#hypertrophy #musclegrowth #strengthtraining #gym #fitness"
    return {"id": 2, "day": 2, "topic": "volume", "scenes": S, "caption": cap, "hashtags": tags,
            "source": "Source: Schoenfeld, Ogborn & Krieger, J Sports Sci, 2017"}

def reel_creatine(handle):
    S = [
        {"type": "hook", "tail": 0.55, "day": 3, "teach_en": "TEACHING YOU: CREATINE",
         "teach_es": "Enseñándote: creatina",
         "title": ["WHAT DOES", "CREATINE DO?"],
         "lines": [L("Day three, teaching you about creatine.", "Día tres, enseñándote sobre la creatina.",
                     ["Day 3, teaching you", "about creatine."], ["Día 3, enseñándote", "sobre la creatina."]),
                   L("What does it do, and is it safe?", "¿Qué hace y es segura?",
                     ["What does it do,", "and is it safe?"], ["¿Qué hace", "y es segura?"])]},
        {"type": "stat", "tail": 0.7, "head": "USUAL DAILY DOSE", "value": "3–5", "ring": 0.5,
         "label": ["grams per day", "creatine monohydrate"],
         "lines": [L("A major sports nutrition society calls creatine monohydrate the most effective supplement for high intensity exercise.",
                     "Una sociedad científica de nutrición deportiva considera a la creatina monohidrato el suplemento más efectivo para el ejercicio de alta intensidad.",
                     ["A major sports nutrition society calls it", "the most effective supplement", "for high intensity exercise."],
                     ["Una sociedad de nutrición deportiva la considera", "el suplemento más efectivo", "para el ejercicio de alta intensidad."]),
                   L("The usual dose is three to five grams per day.", "La dosis habitual es de tres a cinco gramos por día.",
                     ["The usual dose is", "3 to 5 grams per day."], ["La dosis habitual es de", "3 a 5 gramos por día."])]},
        {"type": "tips", "tail": 0.6, "head": "WHAT THE EVIDENCE SAYS",
         "items": [("Helps high-intensity performance and lean mass", "Mejora el rendimiento de alta intensidad y la masa magra"),
                   ("No compelling evidence of harm in healthy people", "Sin evidencia sólida de daño en personas sanas"),
                   ("Loading is optional: 3–5 g a day gets there in 3–4 weeks", "La carga es opcional: 3–5 g al día llegan en 3–4 semanas")],
         "lines": [L("It helps high intensity performance and lean body mass.", "Mejora el rendimiento de alta intensidad y la masa magra.",
                     ["It helps high intensity", "performance and lean mass."], ["Mejora el rendimiento", "de alta intensidad y la masa magra."]),
                   L("Studies found no compelling evidence of harm in healthy people.", "Los estudios no encontraron evidencia sólida de daño en personas sanas.",
                     ["No compelling evidence", "of harm in healthy people."], ["Sin evidencia sólida", "de daño en personas sanas."]),
                   L("A loading phase is optional. Three to five grams a day gets you there in a few weeks.", "La fase de carga es opcional. Con tres a cinco gramos diarios llegas en unas semanas.",
                     ["Loading is optional. 3 to 5 grams a day", "gets you there in a few weeks."], ["La carga es opcional. Con 3 a 5 gramos diarios", "llegas en unas semanas."])]},
        {"type": "cta", "tail": 1.0, "next_en": "DAY 4 TOMORROW: OVERLOAD", "next_es": "Mañana, día 4: sobrecarga progresiva",
         "lines": [L("If you have a medical condition or take medication, ask your doctor first.", "Si tienes una condición médica o tomas medicación, consulta antes con tu médico.",
                     ["If you have a medical condition or", "take medication, ask your doctor first."], ["Si tienes una condición médica o tomas", "medicación, consulta antes a tu médico."]),
                   L("Save this, and come back tomorrow for day four.", "Guárdalo y vuelve mañana para el día cuatro.",
                     ["Save this, and come back", "tomorrow for Day 4."], ["Guárdalo y vuelve mañana", "para el Día 4."])]},
    ]
    cap = (f"Day 3 teaching you: creatine 💪\n"
           f"What does creatine do, and is it safe? The International Society of Sports Nutrition's position stand concludes creatine monohydrate is effective for high-intensity exercise and lean mass, with no compelling evidence of harm in healthy people at studied doses. Usual dose: 3–5 g/day (a loading phase is optional). Ask your doctor first if you have a medical condition or take medication.\n\n"
           f"Día 3 enseñándote: creatina 💪\n"
           f"¿Qué hace la creatina y es segura? La declaración de posición de la Sociedad Internacional de Nutrición Deportiva concluye que la creatina monohidrato es efectiva para el ejercicio de alta intensidad y la masa magra, sin evidencia sólida de daño en personas sanas con las dosis estudiadas. Dosis habitual: 3–5 g/día (la fase de carga es opcional). Si tienes una condición médica o tomas medicación, consulta antes a tu médico.\n\n"
           f"Save this 📌 and follow {handle} — Day 4 tomorrow. / Guárdalo y sigue a {handle}: mañana, Día 4.\n"
           f"Source / Fuente: Kreider et al., J Int Soc Sports Nutr, 2017 (ISSN position stand).\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return {"id": 3, "day": 3, "topic": "creatine", "scenes": S, "caption": cap, "hashtags": "#creatine #supplements #gym #muscle #fitness",
            "source": "Source: Kreider et al., J Int Soc Sports Nutr, 2017"}


def reel_overload(handle):
    S = [
        {"type": "hook", "tail": 0.55, "day": 4, "teach_en": "TEACHING YOU: OVERLOAD",
         "teach_es": "Enseñándote: sobrecarga progresiva",
         "title": ["HOW TO KEEP", "MAKING PROGRESS?"],
         "lines": [L("Day four, teaching you about progressive overload.", "Día cuatro, enseñándote sobre la sobrecarga progresiva.",
                     ["Day 4, teaching you", "about progressive overload."], ["Día 4, enseñándote sobre", "la sobrecarga progresiva."]),
                   L("How do you keep making progress in the gym?", "¿Cómo sigues progresando en el gimnasio?",
                     ["How do you keep making", "progress in the gym?"], ["¿Cómo sigues progresando", "en el gimnasio?"])]},
        {"type": "stat", "tail": 0.7, "head": "PROGRESSIVE OVERLOAD", "value": "2–10%", "vsize": 104, "ring": 0.3,
         "label": ["more load at a time", "ACSM rule of thumb"],
         "lines": [L("Progressive overload means gradually making your training harder over time.", "La sobrecarga progresiva es hacer tu entrenamiento más exigente de forma gradual.",
                     ["Progressive overload means making", "your training gradually harder."], ["La sobrecarga progresiva es hacer", "tu entrenamiento más exigente poco a poco."]),
                   L("The American College of Sports Medicine says progressive training is necessary to keep adapting.", "El Colegio Americano de Medicina del Deporte dice que el entrenamiento progresivo es necesario para seguir adaptándose.",
                     ["The American College of Sports Medicine:", "progression is necessary to keep adapting."], ["El Colegio Americano de Medicina del Deporte:", "progresar es necesario para seguir adaptándose."]),
                   L("Its guideline suggests small jumps, not big ones.", "Su guía sugiere saltos pequeños, no grandes.",
                     ["Its guideline suggests", "small jumps, not big ones."], ["Su guía sugiere", "saltos pequeños, no grandes."])]},
        {"type": "tips", "tail": 0.6, "head": "THE RULE OF THUMB",
         "items": [("Beat your target by 1–2 reps", "Supera tu objetivo por 1–2 repeticiones"),
                   ("Then add 2–10% more load", "Luego suma entre 2 y 10 % de carga"),
                   ("Write it down, so you know when to progress", "Anótalo, para saber cuándo progresar")],
         "lines": [L("First, wait until you can beat your target by one or two reps.", "Primero, espera a poder superar tu objetivo por una o dos repeticiones.",
                     ["First, wait until you can beat", "your target by 1 or 2 reps."], ["Primero, espera a superar tu objetivo", "por una o dos repeticiones."]),
                   L("Then raise the load by two to ten percent.", "Luego sube la carga entre un dos y un diez por ciento.",
                     ["Then raise the load", "by 2 to 10 percent."], ["Luego sube la carga", "entre un 2 y un 10 por ciento."]),
                   L("Track your workouts, so you know when to progress.", "Anota tus entrenamientos, para saber cuándo progresar.",
                     ["Track your workouts,", "so you know when to progress."], ["Anota tus entrenamientos,", "para saber cuándo progresar."])]},
        {"type": "cta", "tail": 1.0, "next_en": "DAY 5 TOMORROW: SLEEP", "next_es": "Mañana, día 5: sueño y recuperación",
         "lines": [L("Save this, and come back tomorrow for day five.", "Guárdalo y vuelve mañana para el día cinco.",
                     ["Save this, and come back", "tomorrow for Day 5."], ["Guárdalo y vuelve mañana", "para el Día 5."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 4 teaching you: progressive overload 💪\n"
           f"How do you keep making progress in the gym? The American College of Sports Medicine's position stand says progressive resistance training is necessary to keep adapting, and suggests a 2–10% increase in load once you can perform the current workload for 1–2 repetitions over the desired number. Small steps, tracked.\n\n"
           f"Día 4 enseñándote: sobrecarga progresiva 💪\n"
           f"¿Cómo sigues progresando en el gimnasio? La declaración de posición del Colegio Americano de Medicina del Deporte dice que el entrenamiento de fuerza progresivo es necesario para seguir adaptándose, y sugiere aumentar la carga entre 2 y 10 % cuando puedes hacer la carga actual con 1–2 repeticiones por encima del objetivo. Pasos pequeños y anotados.\n\n"
           f"Save this 📌 and follow {handle} — Day 5 tomorrow. / Guárdalo y sigue a {handle}: mañana, Día 5.\n"
           f"Source / Fuente: ACSM position stand, Med Sci Sports Exerc, 2009.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return {"id": 4, "day": 4, "topic": "overload", "scenes": S, "caption": cap, "hashtags": "#progressiveoverload #strengthtraining #gym #workout #fitness",
            "source": "Source: ACSM position stand, Med Sci Sports Exerc, 2009"}


def reel_sleep(handle):
    S = [
        {"type": "hook", "tail": 0.55, "day": 5, "teach_en": "TEACHING YOU: SLEEP",
         "teach_es": "Enseñándote: sueño y recuperación",
         "title": ["DOES SLEEP AFFECT", "YOUR MUSCLES?"],
         "lines": [L("Day five, teaching you about sleep and recovery.", "Día cinco, enseñándote sobre el sueño y la recuperación.",
                     ["Day 5, teaching you about", "sleep and recovery."], ["Día 5, enseñándote sobre", "el sueño y la recuperación."]),
                   L("Does sleep really affect your muscles?", "¿El sueño realmente afecta tus músculos?",
                     ["Does sleep really", "affect your muscles?"], ["¿El sueño realmente", "afecta tus músculos?"])]},
        {"type": "stat", "tail": 0.7, "head": "ONE NIGHT WITHOUT SLEEP", "value": "\u221218%", "vsize": 150, "ring": 0.18,
         "label": ["muscle protein synthesis", "in a small study"],
         "lines": [L("In a small study of thirteen healthy young adults, one night without sleep reduced muscle protein synthesis by eighteen percent.",
                     "En un estudio pequeño de trece adultos jóvenes sanos, una noche sin dormir redujo la síntesis de proteína muscular un dieciocho por ciento.",
                     ["In a small study of 13 young adults,", "one night without sleep cut muscle", "protein synthesis by 18%."],
                     ["En un estudio de 13 adultos jóvenes,", "una noche sin dormir redujo", "la síntesis de proteína muscular un 18 %."]),
                   L("Cortisol rose twenty-one percent, and testosterone fell twenty-four percent.",
                     "El cortisol subió un veintiuno por ciento y la testosterona bajó un veinticuatro por ciento.",
                     ["Cortisol rose 21%,", "and testosterone fell 24%."], ["El cortisol subió un 21 %", "y la testosterona bajó un 24 %."])]},
        {"type": "tips", "tail": 0.6, "head": "WHAT TO TAKE FROM THIS",
         "items": [("Adults: aim for 7 or more hours a night", "Adultos: apunta a 7 horas o más por noche"),
                   ("That study was small and measured just one night", "El estudio fue pequeño y midió solo una noche"),
                   ("Sleep is one piece: training and protein still matter", "El sueño es una pieza: entrenar y la proteína siguen importando")],
         "lines": [L("Sleep experts recommend that adults get seven or more hours a night.", "Los expertos en sueño recomiendan que los adultos duerman siete horas o más por noche.",
                     ["Sleep experts recommend adults", "get 7 or more hours a night."], ["Los expertos recomiendan que los adultos", "duerman 7 horas o más por noche."]),
                   L("Keep in mind, that study was small, and it measured just one night.", "Ten en cuenta que ese estudio fue pequeño y midió solo una noche.",
                     ["Keep in mind, that study was small,", "and measured just one night."], ["Ese estudio fue pequeño", "y midió solo una noche."]),
                   L("Sleep is one piece of the puzzle. Training and protein still matter.", "El sueño es una pieza del rompecabezas. Entrenar y la proteína siguen importando.",
                     ["Sleep is one piece of the puzzle.", "Training and protein still matter."], ["El sueño es una pieza del rompecabezas.", "Entrenar y la proteína siguen importando."])]},
        {"type": "cta", "tail": 1.0, "next_en": "DAY 6 TOMORROW: CALORIES", "next_es": "Mañana, día 6: déficit calórico",
         "lines": [L("Save this, and come back tomorrow for day six.", "Guárdalo y vuelve mañana para el día seis.",
                     ["Save this, and come back", "tomorrow for Day 6."], ["Guárdalo y vuelve mañana", "para el Día 6."]),
                   L("Follow for one new lesson every day.", "Sígueme para una lección nueva cada día.",
                     ["Follow for one new lesson", "every day."], ["Sígueme para una lección", "nueva cada día."])]},
    ]
    cap = (f"Day 5 teaching you: sleep and recovery 💪\n"
           f"Does sleep really affect your muscles? In a small randomized crossover study of 13 healthy young adults, one night of total sleep deprivation reduced muscle protein synthesis by 18%, raised cortisol 21% and lowered testosterone 24%. It was a single night in a small sample, so don't over-read it. Sleep experts (AASM/SRS) recommend adults sleep 7+ hours per night.\n\n"
           f"Día 5 enseñándote: sueño y recuperación 💪\n"
           f"¿El sueño realmente afecta tus músculos? En un estudio cruzado aleatorizado pequeño de 13 adultos jóvenes sanos, una noche sin dormir redujo la síntesis de proteína muscular un 18 %, subió el cortisol 21 % y bajó la testosterona 24 %. Fue una sola noche en una muestra pequeña, así que no hay que sobreinterpretarlo. Los expertos (AASM/SRS) recomiendan que los adultos duerman 7 horas o más por noche.\n\n"
           f"Save this 📌 and follow {handle} — Day 6 tomorrow. / Guárdalo y sigue a {handle}: mañana, Día 6.\n"
           f"Source / Fuente: Lamon et al., Physiol Rep, 2021; AASM/SRS consensus, 2015.\n"
           f"Educational content, not medical advice. / Contenido educativo, no es consejo médico.")
    return {"id": 5, "day": 5, "topic": "sleep", "scenes": S, "caption": cap, "hashtags": "#sleep #recovery #musclegrowth #gym #fitness",
            "source": "Source: Lamon et al., Physiol Rep, 2021; AASM/SRS, 2015"}


REELS = {2: reel_volume, 3: reel_creatine, 4: reel_overload, 5: reel_sleep}


def render(reel, handle, voice, out_dir, stem):
    global Q, DAY
    Q = reel.get("q", 0); DAY = reel["day"]
    scenes = reel["scenes"]
    t = 0.0; vparts = []
    for sc in scenes:
        sc["t0"] = t; lt = t + LEAD; sc["_lines"] = []
        for ln in sc["lines"]:
            a = voice.say(ln["en"]); ln = dict(ln)
            ln["audio"] = a; ln["t0"] = lt; ln["t1"] = lt + len(a) / SR; lt = ln["t1"] + GAP
            sc["_lines"].append(ln)
        sc["t1"] = lt - GAP + sc["tail"]; t = sc["t1"]
    total = t
    voice_tr = np.zeros(int(total * SR) + SR, dtype=np.float32)
    for sc in scenes:
        for ln in sc["_lines"]:
            i = int(ln["t0"] * SR); voice_tr[i:i + len(ln["audio"])] += ln["audio"]
    os.makedirs(out_dir, exist_ok=True)
    wav = os.path.join(out_dir, stem + ".wav")
    prev = os.environ.get("PREVIEW")
    if not prev:
        synth_audio(scenes, total, voice_tr, wav, seed=DAY, day=DAY)
    # boca desde la envolvente de la voz
    nF = int(math.ceil(total * FPS)); hop = SR // FPS
    mo = np.array([np.sqrt(np.mean(voice_tr[i * hop:i * hop + hop] ** 2)) if i * hop < len(voice_tr) else 0 for i in range(nF)])
    mo = np.clip(mo / (np.percentile(mo[mo > 0.005], 90) if (mo > 0.005).any() else 1) * 0.95, 0, 1)
    mo = np.convolve(mo, [0.3, 0.4, 0.3], mode="same")
    # fondo estatico
    ys = np.linspace(0, 1, H)[:, None, None]
    top = np.array([30, 20, 26]); bot = np.array([14, 10, 12])
    bg = (top * (1 - ys) + bot * ys) * np.ones((1, W, 1))
    bgi = Image.fromarray(bg.astype(np.uint8))
    gd = ImageDraw.Draw(bgi)
    for cx, cy, r, c in ((880, 260, 360, (44, 28, 24)), (120, 1050, 420, (26, 28, 40)), (900, 1500, 380, (42, 24, 22))):
        for k in range(10):
            rr = r * (1 - k / 10); gd.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=mix(bg[min(H - 1, cy), 0].astype(int).tolist(), c, (k + 1) / 10))
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-i", wav, "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
           "-ar", "48000", "-movflags", "+faststart", "-shortest", os.path.join(out_dir, stem + ".mp4")]
    pr = None if prev else subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_pose = POSES["idle"]; cur_idx = -1; pose_from = POSES["idle"]
    f40 = get_font(40); f26 = get_font(26)
    rng = np.random.default_rng(5)
    dots = [(rng.uniform(0, W), rng.uniform(0, H), rng.uniform(0.3, 1), rng.uniform(4, 10)) for _ in range(26)]
    t_start = time.time()
    frames_iter = [min(nF - 1, int(float(x) * FPS)) for x in prev.split(",")] if prev else range(nF)
    for fi in frames_iter:
        tt = fi / FPS
        si = next(i for i, s in enumerate(scenes) if tt < s["t1"] or i == len(scenes) - 1)
        sc = scenes[si]; lt = tt - sc["t0"]
        img = bgi.copy(); d = ImageDraw.Draw(img)
        if Q >= 2:
            living_bg(img, d, tt)
        else:
            for (x, y, sp, r) in dots:
                yy = (y - tt * 40 * sp) % H
                d.ellipse([x - r, yy - r, x + r, yy + r], fill=(46, 34, 36))
        txt(d, (540, 118), f"{BRAND}  ·  DAY {reel['id']}", f40, ORANGE)
        if Q >= 5: tracker(d, reel["day"])
        if sc["type"] == "cta":
            sc["_h"] = handle
        tl = {"handle": handle}
        SCENES[sc["type"]](img, d, sc, lt, tl, tt)
        pname, my, ms, mx_ = MASCOT[sc["type"]]
        if si != cur_idx:
            cur_idx = si; pose_from = prev_pose
        pose = lerp_pose(pose_from, POSES[pname], ease_out(lt / 0.4)); prev_pose = pose
        sbounce = ms * (1 + 0.06 * max(0, math.sin(min(lt, 0.4) / 0.4 * math.pi)))
        sweat = pname == "flex" and lt > 0.8
        extra = {}
        if Q >= 6 and sc.get("anim"):
            pose, extra = anim_state(sc["anim"], tt)
        dy = extra.pop("dy", 0)
        draw_mascot(img, mx_, my + dy, sbounce, tt, mouth=float(mo[fi]), pose=pose, blink=blink_factor(tt), look=(math.sin(tt * 0.8) * 0.5, 0),
                    flex_sweat=sweat, medal=(Q >= 7 and sc["type"] in ("recap", "cta")), **extra)
        if Q >= 7: vignette(img)
        if Q >= 4:
            img = zoom_img(img, 1 + 0.035 * min(1.0, lt / max(1.0, sc["t1"] - sc["t0"])))
        d = ImageDraw.Draw(img)
        if Q >= 1:
            if si > 0: wipe(d, lt)
            d.rounded_rectangle([60, 1790, 1020, 1798], radius=4, fill=(54, 42, 48))
            d.rounded_rectangle([60, 1790, 60 + 8 + 952 * tt / total, 1798], radius=4, fill=ORANGE)
        draw_subs(img, d, scenes, tt)
        d = ImageDraw.Draw(img)
        txt(d, (540, 1815), "Educational content, not medical advice", f26, MUTED)
        txt(d, (540, 1850), reel["source"], fit_font(d, reel["source"], 980, 26, 16), MUTED)
        if fi == int(1.0 * FPS):
            img.save(os.path.join(out_dir, stem + "_cover.jpg"), quality=90)
        if prev: img.save(os.path.join(out_dir, f"prev_{fi}.png"))
        else: pr.stdin.write(img.tobytes())
        if fi % 150 == 0:
            print(f"frame {fi}/{nF}  {time.time() - t_start:.0f}s", flush=True)
    if pr: pr.stdin.close(); pr.wait()
    if prev: return
    meta = {"id": reel["id"], "duration": round(total, 2), "caption": reel["caption"], "hashtags": reel["hashtags"],
            "lines": [{"t0": round(l["t0"], 2), "t1": round(l["t1"], 2), "en": l["en"]} for s in scenes for l in s["_lines"]]}
    json.dump(meta, open(os.path.join(out_dir, stem + ".json"), "w"), ensure_ascii=False, indent=1)
    print("OK", stem, f"{total:.1f}s")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--day", type=int, default=2)
    ap.add_argument("--handle", default="@gains.labb")
    ap.add_argument("--out", default="out")
    ap.add_argument("--model-dir", default="/home/claude/tts/kokoro-multi-lang-v1_0")
    ap.add_argument("--sid", type=int, default=3)
    ap.add_argument("--speed", type=float, default=1.05)
    a = ap.parse_args()
    import reels_more
    REELS.update(reels_more.REELS_MORE)
    import reels_more2
    REELS.update(reels_more2.REELS_MORE2)
    reel = REELS[a.day](a.handle)
    v = Voice(a.model_dir, a.sid, a.speed, os.path.join(a.out, "cache"))
    render(reel, a.handle, v, a.out, f"fit_{reel['id']:03d}_{reel['topic']}_en")
