#!/usr/bin/env python3
"""Publicador diario de Reels de @gains.labb.
Reglas: 1 Reel por fecha de Buenos Aires; el dia N+1 solo despues de verificar el dia N; nunca sustituye videos;
estado persistente en schedule.json (el workflow lo commitea tras cada intento); reintentos sin duplicar."""
import argparse, datetime as dt, json, os, subprocess, sys, time, urllib.request, urllib.error
from zoneinfo import ZoneInfo
sys.path.insert(0, os.path.dirname(__file__))
from igapi import IG, ApiError

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHED = os.path.join(ROOT, "schedule.json")
TZ = ZoneInfo("America/Argentina/Buenos_Aires")
LOG = os.path.join(ROOT, "logs", "publish.log")

def now():
    o = os.environ.get("NOW_OVERRIDE")  # solo para pruebas, ISO con offset
    return dt.datetime.fromisoformat(o).astimezone(TZ) if o else dt.datetime.now(TZ)

def log(msg):
    line = f"{now().isoformat(timespec='seconds')} {msg}"
    print(line, flush=True)
    os.makedirs(os.path.dirname(LOG), exist_ok=True)
    with open(LOG, "a", encoding="utf-8") as f: f.write(line + "\n")

def load():  return json.load(open(SCHED, encoding="utf-8"))
def save(c):
    tmp = SCHED + ".tmp"
    json.dump(c, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    os.replace(tmp, SCHED)

def err(d, where, e):
    d["errors"].append({"at": now().isoformat(timespec="seconds"), "where": where, "error": str(e)[:500]})

def validate_video(d):
    p = os.path.join(ROOT, d["video"])
    if not os.path.isfile(p): return "archivo inexistente: " + d["video"]
    size = os.path.getsize(p)
    if size < 100_000: return f"archivo demasiado pequeno ({size} B)"
    if size > 300 * 1024 * 1024: return "supera 300 MB"
    with open(p, "rb") as f:
        if f.read(12)[4:8] != b"ftyp": return "no parece un MP4 (falta ftyp)"
    try:
        out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
            "stream=codec_name,width,height:format=duration", "-of", "json", p], capture_output=True, text=True, timeout=60)
        if out.returncode == 0:
            j = json.loads(out.stdout); s = j["streams"][0]; dur = float(j["format"]["duration"])
            if s["codec_name"] != "h264": return "codec no h264"
            if (s["width"], s["height"]) != (1080, 1920): return f"resolucion {s['width']}x{s['height']}"
            if not 3 <= dur <= 90: return f"duracion {dur:.1f}s fuera de 3-90s"
        elif not os.environ.get("ALLOW_NO_FFPROBE"): return "ffprobe fallo: " + out.stderr[:200]
    except FileNotFoundError:
        if not os.environ.get("ALLOW_NO_FFPROBE"): return "ffprobe no disponible"
    return None

def video_url(d):
    base = os.environ.get("PAGES_BASE_URL", "").rstrip("/")
    if not base: raise ApiError("Falta PAGES_BASE_URL (URL publica de GitHub Pages)")
    return f"{base}/{d['video']}"

def check_public(url):
    req = urllib.request.Request(url, method="HEAD")
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            ct = r.headers.get("Content-Type", "")
            if r.status != 200: return f"HTTP {r.status}"
            if "video" not in ct and "octet" not in ct: return f"Content-Type inesperado: {ct}"
    except Exception as e:
        return f"no accesible: {e}"
    return None

def wait_container(ig, cid, d, max_s):
    t0 = time.time()
    while True:
        st = ig.container_status(cid)
        code = st.get("status_code")
        log(f"dia {d['day']}: contenedor {cid} -> {code}")
        if code == "FINISHED": return True
        if code in ("ERROR", "EXPIRED"): raise ApiError(f"contenedor {code}: {st.get('status')}")
        if time.time() - t0 > max_s: raise ApiError("timeout esperando al contenedor")
        time.sleep(float(os.environ.get("POLL_SECONDS", "30")))

def find_already_published(ig, d):
    """Evita doble publicacion si media_publish se ejecuto pero no llegamos a registrarlo."""
    head = d["caption"].strip().split("\n")[0][:60]
    for m in ig.recent_media(25):
        if m.get("media_product_type") in ("REELS", None) and (m.get("caption") or "").strip().startswith(head):
            return m["id"]
    return None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="valida todo, no llama a Instagram")
    ap.add_argument("--force", action="store_true", help="ignora la espera hasta las 19:00 (uso manual)")
    ap.add_argument("--status", action="store_true")
    a = ap.parse_args()
    c = load(); n = now(); today = n.date().isoformat()
    days = sorted(c["days"], key=lambda x: x["day"])
    if a.status:
        for d in days: print(d["day"], d["planned_date"], d["publish_status"], d["ig_media_id"], d["comment_status"])
        return 0
    # dia actual = primero no publicado; los siguientes quedan bloqueados hasta verificar este
    cur = next((d for d in days if d["publish_status"] != "published"), None)
    if cur is None:
        log("Calendario completo: no hay dias pendientes. Faltan contenidos (Dia 13+)."); return 0
    if any(d["publish_status"] == "published" and d.get("published_date") == today for d in days):
        log(f"Ya se publico un Reel hoy ({today}); no se publica otro."); return 0
    if cur["planned_date"] > today:
        log(f"Dia {cur['day']} esta previsto para {cur['planned_date']}; hoy es {today}. Nada que hacer."); return 0
    late = cur["planned_date"] < today
    # espera hasta las 19:00 ART
    target = dt.datetime.combine(n.date(), dt.time(19, 0), TZ)
    if n < target and not a.force:
        wait = (target - n).total_seconds()
        if wait > 3 * 3600: log(f"Faltan {wait/3600:.1f} h para las 19:00; salgo."); return 0
        log(f"Esperando {wait:.0f}s hasta las 19:00 ART"); 
        if not a.dry_run and not os.environ.get("SKIP_WAIT"): time.sleep(wait)
    log(f"Dia {cur['day']} (previsto {cur['planned_date']}{', ATRASADO' if late else ''}) -> inicio")
    cur["attempts"] += 1

    problem = validate_video(cur)
    if problem:
        cur["generation_status"] = "missing_or_invalid"; err(cur, "validate", problem); save(c)
        log(f"ERROR video dia {cur['day']}: {problem}. NO se publica ni se sustituye."); return 2
    cur["generation_status"] = "ready"
    if not cur["caption"].strip() or len(cur["caption"]) > 2200:
        err(cur, "caption", "caption vacio o >2200"); save(c); return 2
    if a.dry_run:
        log(f"DRY-RUN ok: dia {cur['day']} video valido, caption {len(cur['caption'])} caracteres, url {os.environ.get('PAGES_BASE_URL','(sin PAGES_BASE_URL)')}/{cur['video']}")
        cur["attempts"] -= 1; return 0

    tok, igid = os.environ.get("IG_ACCESS_TOKEN"), os.environ.get("IG_USER_ID")
    if not tok or not igid:
        err(cur, "auth", "Faltan secretos IG_ACCESS_TOKEN / IG_USER_ID"); save(c); log("ERROR: faltan secretos"); return 3
    ig = IG(tok, igid)
    try:
        # 1) ya publicado pero sin registrar?
        if cur["publish_status"] == "publishing":
            mid = find_already_published(ig, cur)
            if mid:
                log(f"Detectado Reel ya publicado ({mid}); se registra sin republicar.")
                cur.update(publish_status="published", ig_media_id=mid, published_at=now().isoformat(timespec="seconds"), published_date=today)
                save(c)
            else:
                log("Estado 'publishing' sin Reel en la cuenta: se reintenta con un contenedor nuevo."); cur["ig_container_id"] = None
        if cur["publish_status"] != "published":
            # 2) contenedor
            if not cur["ig_container_id"]:
                url = video_url(cur)
                bad = check_public(url)
                if bad: raise ApiError(f"URL publica del video no valida ({url}): {bad}")
                cur["ig_container_id"] = ig.create_reel(url, cur["caption"]); cur["publish_status"] = "container_created"; save(c)
                log(f"Contenedor creado {cur['ig_container_id']}")
            wait_container(ig, cur["ig_container_id"], cur, float(os.environ.get("CONTAINER_TIMEOUT", "600")))
            # 3) publicar (marcamos antes para poder recuperarnos de un corte justo despues)
            cur["publish_status"] = "publishing"; save(c)
            mid = ig.publish(cur["ig_container_id"])
            cur.update(publish_status="published", ig_media_id=mid, published_at=now().isoformat(timespec="seconds"), published_date=today)
            save(c); log(f"PUBLICADO dia {cur['day']} -> media {mid}")
    except ApiError as e:
        err(cur, "publish", e)
        if cur["publish_status"] == "publishing":
            pass  # incierto: el proximo intento comprobara la cuenta antes de reintentar
        elif cur["publish_status"] == "container_created" and ("EXPIRED" in str(e) or "ERROR" in str(e)):
            cur["ig_container_id"] = None; cur["publish_status"] = "pending"
        save(c); log(f"ERROR publicando dia {cur['day']}: {e}"); return 4

    # 4) comentario inicial (un fallo aqui NO invalida la publicacion ni bloquea el calendario)
    if cur["comment_status"] != "posted":
        try:
            cur["comment_id"] = ig.comment(cur["ig_media_id"], cur["first_comment"]); cur["comment_status"] = "posted"
            log(f"Comentario publicado {cur['comment_id']}. Fijado: no soportado por la API oficial (hacerlo a mano si se desea).")
        except ApiError as e:
            cur["comment_status"] = "failed"; err(cur, "comment", e); log(f"AVISO comentario fallo: {e}")
        save(c)
    return 0

if __name__ == "__main__":
    sys.exit(main())
