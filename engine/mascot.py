"""mascot.py -- personaje 'frijol naranja' dibujado por codigo (sin assets externos)."""
import math
from PIL import Image, ImageDraw

BODY = (255, 146, 46)
BODY_D = (233, 112, 22)
BODY_L = (255, 184, 104)
BAND = (222, 40, 52)
WHITE = (252, 250, 245)
DARK = (44, 24, 22)
CHEEK = (255, 118, 118)
SHOE = (38, 40, 56)
SOLE = (245, 245, 245)

# pose = (angulo hombro der, angulo codo der, angulo hombro izq, angulo codo izq); 0 = hacia abajo, 90 = horizontal, 180 = arriba
POSES = {
    "idle":    (22, 16, 22, 16),
    "wave":    (118, 160, 20, 14),
    "present": (22, 14, 78, 66),
    "point":   (24, 16, 82, 84),
    "cheer":   (140, 172, 140, 172),
    "flex":    (92, 176, 92, 176),
}


def lerp_pose(a, b, k):
    return tuple(a[i] + (b[i] - a[i]) * k for i in range(4))


def blink_factor(t, period=3.4):
    ph = t % period
    if ph < 0.14:
        return abs(ph - 0.07) / 0.07
    return 1.0


def _arm(d, sx, side, a1, a2, k, wob=0.0):
    """Brazo de dos segmentos. side=+1 derecha del personaje (x+), -1 izquierda."""
    L1, L2 = 96, 86
    r1 = math.radians(a1 + wob)
    r2 = math.radians(a2 + wob * 1.6)
    ex, ey = sx + side * math.sin(r1) * L1, 30 + math.cos(r1) * L1
    hx, hy = ex + side * math.sin(r2) * L2, ey + math.cos(r2) * L2
    w = 34
    d.line([(sx * k, 30 * k), (ex * k, ey * k)], fill=BODY_D, width=int(w * k))
    d.line([(ex * k, ey * k), (hx * k, hy * k)], fill=BODY_D, width=int(w * k))
    d.line([(sx * k, 30 * k), (ex * k, ey * k)], fill=BODY, width=int((w - 8) * k))
    d.line([(ex * k, ey * k), (hx * k, hy * k)], fill=BODY, width=int((w - 8) * k))
    for (px, py, r) in ((ex, ey, 17), (sx, 30, 17)):
        d.ellipse([(px - r) * k, (py - r) * k, (px + r) * k, (py + r) * k], fill=BODY)
    g = 30
    d.ellipse([(hx - g) * k, (hy - g) * k, (hx + g) * k, (hy + g) * k], fill=WHITE, outline=(205, 200, 190), width=int(3 * k))


def draw_mascot(img, cx, cy, s, t, mouth=0.0, pose=None, blink=1.0, look=(0, 0), flex_sweat=False, spread=0, squash=1.0, medal=False):
    """Dibuja el personaje centrado en (cx,cy) del cuerpo, escala s."""
    SS = 2
    k = SS * s
    cw, ch = int(820 * k), int(980 * k)
    ox, oy = cw / 2, 470 * k          # origen local dentro del lienzo
    can = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d = ImageDraw.Draw(can)

    class _K:  # traduce coordenadas locales -> lienzo
        pass

    # Trabajamos trasladando: dibujamos en un lienzo auxiliar con origen en (0,0) y pegamos con offset
    can2 = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    d2 = ImageDraw.Draw(can2)

    bob = math.sin(t * 5.2) * 5
    pose = pose or POSES["idle"]
    # Para simplificar, todo se dibuja con origen local (0,0) = centro del cuerpo y se desplaza con 'off'
    off = (ox, oy + bob * k)

    def E(x0, y0, x1, y1, **kw):
        d2.ellipse([off[0] + x0 * k, off[1] + y0 * k, off[0] + x1 * k, off[1] + y1 * k], **kw)

    # sombra
    sh = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    ImageDraw.Draw(sh).ellipse([ox - 150 * k, oy + 255 * k, ox + 150 * k, oy + 295 * k], fill=(0, 0, 0, 70))
    can2.alpha_composite(sh)

    # piernas y zapatillas
    for sx in (-(72 + spread), 72 + spread):
        d2.rectangle([off[0] + (sx - 14) * k, off[1] + 170 * k, off[0] + (sx + 14) * k, off[1] + 225 * k], fill=BODY_D)
        E(sx - 62, 205, sx + 62, 262, fill=SOLE)
        E(sx - 58, 200, sx + 58, 252, fill=SHOE)
        E(sx - 30, 208, sx + 22, 226, fill=(80, 84, 110))

    # brazos (detras del cuerpo)
    wob = math.sin(t * 9) * 9 if pose[1] > 150 and pose[3] < 60 else 0
    # compensar pequena animacion respiracion
    ar = pose
    # el brazo derecho del personaje va hacia x+; se dibuja con offset de lienzo
    class _D:
        pass
    # dibujamos brazos en un lienzo temporal con origen = off
    arms = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    da = ImageDraw.Draw(arms)

    def arm(side, a1, a2, w_):
        # coordenadas locales -> trasladadas por off
        L1, L2 = 96, 86
        sx = side * 158
        r1 = math.radians(a1 + w_)
        r2 = math.radians(a2 + w_ * 1.6)
        ex, ey = sx + side * math.sin(r1) * L1, 30 + math.cos(r1) * L1
        hx, hy = ex + side * math.sin(r2) * L2, ey + math.cos(r2) * L2

        def P(x, y):
            return (off[0] + x * k, off[1] + y * k)
        da.line([P(sx, 30), P(ex, ey)], fill=BODY_D, width=int(36 * k))
        da.line([P(ex, ey), P(hx, hy)], fill=BODY_D, width=int(36 * k))
        da.line([P(sx, 30), P(ex, ey)], fill=BODY, width=int(28 * k))
        da.line([P(ex, ey), P(hx, hy)], fill=BODY, width=int(28 * k))
        for (px, py) in ((ex, ey), (sx, 30)):
            da.ellipse([P(px - 14, py - 14), P(px + 14, py + 14)], fill=BODY)
        g = 31
        da.ellipse([P(hx - g, hy - g), P(hx + g, hy + g)], fill=WHITE, outline=(205, 200, 190), width=int(3 * k))
        # dedos sugeridos
        da.arc([P(hx - 14, hy - 12), P(hx + 14, hy + 16)], 20, 160, fill=(215, 210, 200), width=int(3 * k))

    arm(1, ar[0], ar[1], wob)
    arm(-1, ar[2], ar[3], 0)
    can2.alpha_composite(arms)

    # cuerpo
    E(-172, -215, 172, 205, fill=BODY_D)
    E(-168, -222, 168, 190, fill=BODY)
    E(-120, -190, -30, -110, fill=BODY_L)           # brillo
    E(-110, 90, 110, 196, fill=(255, 160, 70))      # panza
    if medal:
        d2.polygon([(off[0] - 40 * k, off[1] + 20 * k), (off[0] - 8 * k, off[1] + 20 * k), (off[0] + 14 * k, off[1] + 112 * k), (off[0] - 18 * k, off[1] + 112 * k)], fill=(60, 120, 230))
        d2.polygon([(off[0] + 40 * k, off[1] + 20 * k), (off[0] + 8 * k, off[1] + 20 * k), (off[0] - 14 * k, off[1] + 112 * k), (off[0] + 18 * k, off[1] + 112 * k)], fill=(230, 60, 70))
        E(-38, 100, 38, 176, fill=(214, 160, 20))
        E(-30, 108, 30, 168, fill=(255, 214, 70))
        d2.polygon([(off[0] + p[0] * k, off[1] + p[1] * k) for p in [(0, 116), (7, 133), (26, 135), (12, 147), (16, 165), (0, 155), (-16, 165), (-12, 147), (-26, 135), (-7, 133)]], fill=(214, 160, 20))

    # cinta roja
    band = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    db = ImageDraw.Draw(band)
    db.rounded_rectangle([off[0] - 168 * k, off[1] - 150 * k, off[0] + 168 * k, off[1] - 104 * k], radius=int(20 * k), fill=BAND)
    mask = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(mask).ellipse([off[0] - 168 * k, off[1] - 222 * k, off[0] + 168 * k, off[1] + 190 * k], fill=255)
    bl = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
    bl.paste(band, (0, 0), mask)
    can2.alpha_composite(bl)
    sw = math.sin(t * 6) * 6
    for sgn, ln in ((1, 80), (1, 64)):
        pass
    d2.polygon([(off[0] + 150 * k, off[1] - 128 * k), (off[0] + (225 + sw) * k, off[1] - 168 * k),
                (off[0] + (212 + sw) * k, off[1] - 118 * k)], fill=BAND)
    d2.polygon([(off[0] + 150 * k, off[1] - 128 * k), (off[0] + (232 + sw) * k, off[1] - 100 * k),
                (off[0] + (205 + sw) * k, off[1] - 88 * k)], fill=(190, 28, 40))

    # ojos
    lx, ly = look
    for ex_ in (-62, 62):
        hh = 46 * max(0.08, blink)
        E(ex_ - 38, -50 - hh, ex_ + 38, -50 + hh, fill=WHITE)
        if blink > 0.3:
            E(ex_ - 20 + lx * 8, -50 - 22 * blink + ly * 6, ex_ + 20 + lx * 8, -50 + 22 * blink + ly * 6, fill=DARK)
            E(ex_ - 8 + lx * 8, -50 - 16 * blink + ly * 6, ex_ + 4 + lx * 8, -50 - 4 * blink + ly * 6, fill=WHITE)
    # cejas amigables
    for sgn in (-1, 1):
        d2.arc([off[0] + (sgn * 62 - 44) * k, off[1] - 128 * k, off[0] + (sgn * 62 + 44) * k, off[1] - 70 * k],
               200, 340, fill=DARK, width=int(7 * k))
    # mejillas
    E(-128, 0, -84, 30, fill=CHEEK)
    E(84, 0, 128, 30, fill=CHEEK)
    # boca
    m = max(0.0, min(1.0, mouth))
    mh = 8 + m * 56
    mw = 62 + m * 16
    if m < 0.06:
        d2.arc([off[0] - 46 * k, off[1] + 6 * k, off[0] + 46 * k, off[1] + 64 * k], 20, 160, fill=DARK, width=int(8 * k))
    else:
        E(-mw / 2, 36, mw / 2, 36 + mh, fill=DARK)
        E(-mw / 2 + 10, 36 + mh * 0.5, mw / 2 - 10, 36 + mh, fill=(236, 96, 110))
        d2.rectangle([off[0] + (-mw / 2 + 12) * k, off[1] + 38 * k, off[0] + (mw / 2 - 12) * k, off[1] + 46 * k], fill=WHITE)
    if flex_sweat:
        E(176, -90, 200, -50, fill=(120, 205, 255))

    can2 = can2.resize((int(cw / SS), int(ch / SS)), Image.LANCZOS)
    px = int(cx - (cw / SS) / 2)
    py = int(cy - (470 * s))
    if squash != 1.0:
        nh = int(can2.size[1] * squash)
        can2 = can2.resize((can2.size[0], nh), Image.BILINEAR)
        py = int(cy - 470 * s + (1 - squash) * 732 * s)
    img.paste(can2, (px, py), can2)
