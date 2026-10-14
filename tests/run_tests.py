#!/usr/bin/env python3
"""Pruebas del flujo completo contra el servidor simulado. No publica nada real."""
import json, os, shutil, subprocess, sys, tempfile, urllib.request
HERE = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE); import mock_meta
PORT = 8765; srv = mock_meta.serve(PORT); S = mock_meta.S
def mk():
    d = tempfile.mkdtemp(); shutil.copytree(os.path.join(REPO, "autopost"), d + "/autopost", ignore=shutil.ignore_patterns("__pycache__"))
    shutil.copy(REPO + "/schedule.json", d); os.symlink(REPO + "/videos", d + "/videos"); return d
def run(d, now, token="GOOD", extra=(), env=None):
    e = dict(os.environ, IG_ACCESS_TOKEN=token, IG_USER_ID="123", IG_API_BASE=f"http://127.0.0.1:{PORT}",
             PAGES_BASE_URL=f"http://127.0.0.1:{PORT}", NOW_OVERRIDE=now, SKIP_WAIT="1", POLL_SECONDS="0", **(env or {}))
    r = subprocess.run([sys.executable, d + "/autopost/publish.py", *extra], capture_output=True, text=True, env=e)
    return r.returncode, json.load(open(d + "/schedule.json"))
def day(c, n): return next(x for x in c["days"] if x["day"] == n)
ok = 0
def check(name, cond):
    global ok; print(("PASS " if cond else "FAIL ") + name); ok += 0 if cond else 1
def reset(): S.update(containers={}, media=[], comments=[], fail_publish_once=False, crash_after_publish=False, n=0)

# 1 antes de las 19:00 y lejos: no publica
reset(); d = mk(); rc, c = run(d, "2026-10-14T09:00:00-03:00")
check("1. a las 09:00 no publica (faltan >3h)", rc == 0 and day(c, 8)["publish_status"] == "pending" and not S["media"])
# 2 18:50 espera y publica a las 19:00 (espera simulada)
rc, c = run(d, "2026-10-14T18:50:00-03:00")
check("2. Dia 8 publicado + comentario", rc == 0 and day(c, 8)["publish_status"] == "published" and day(c, 8)["comment_status"] == "posted" and len(S["media"]) == 1)
check("2b. caption y video correctos", S["containers"]["c1"]["video_url"].endswith("videos/dia08_frecuencia.mp4") and "#trainingfrequency" in S["containers"]["c1"]["caption"])
check("2c. pin marcado no soportado (no simulado)", day(c, 8)["pin_status"] == "not_supported_by_api")
# 3 reintento el mismo dia: no duplica
rc, c = run(d, "2026-10-14T19:30:00-03:00")
check("3. segundo intento el mismo dia no duplica", len(S["media"]) == 1 and day(c, 9)["publish_status"] == "pending")
# 4 dia siguiente publica Dia 9, no se salta
rc, c = run(d, "2026-10-15T19:05:00-03:00")
check("4. 15/10 publica Dia 9", day(c, 9)["publish_status"] == "published" and len(S["media"]) == 2)
# 5 fallo de publish: no avanza, reintenta sin duplicar
reset(); d = mk(); S["fail_publish_once"] = True
rc, c = run(d, "2026-10-14T19:01:00-03:00")
check("5. fallo -> dia 8 no queda publicado, error registrado, rc!=0", rc != 0 and day(c, 8)["publish_status"] == "publishing" and day(c, 8)["errors"] and not S["media"])
rc, c = run(d, "2026-10-14T19:21:00-03:00")
check("5b. reintento publica una sola vez", day(c, 8)["publish_status"] == "published" and len(S["media"]) == 1 and day(c, 9)["publish_status"] == "pending")
# 6 caida justo tras publicar: el reintento detecta el Reel y no duplica
reset(); d = mk(); S["crash_after_publish"] = True
rc, c = run(d, "2026-10-14T19:01:00-03:00")
check("6. corte tras publish: quedo 'publishing'", day(c, 8)["publish_status"] == "publishing" and len(S["media"]) == 1)
rc, c = run(d, "2026-10-14T19:21:00-03:00")
check("6b. reintento detecta Reel existente, no duplica", day(c, 8)["publish_status"] == "published" and day(c, 8)["ig_media_id"] == "mc1" and len(S["media"]) == 1 and len(S["containers"]) == 1)
# 7 video faltante: no publica, no sustituye, no avanza
reset(); d = mk(); os.unlink(d + "/videos"); os.mkdir(d + "/videos")
for n in (9, 10, 11, 12): pass
shutil.copy(REPO + "/videos/dia09_repeticiones.mp4", d + "/videos/")
rc, c = run(d, "2026-10-14T19:01:00-03:00")
check("7. falta video dia 8: rc!=0, nada publicado, dia 9 no se usa", rc == 2 and not S["media"] and day(c, 8)["generation_status"] == "missing_or_invalid" and day(c, 9)["publish_status"] == "pending")
# 8 video corrupto
open(d + "/videos/dia08_frecuencia.mp4", "wb").write(b"\x00" * 200000)
rc, c = run(d, "2026-10-14T19:02:00-03:00")
check("8. video corrupto rechazado", rc == 2 and not S["media"])
# 9 token invalido
reset(); d = mk(); rc, c = run(d, "2026-10-14T19:01:00-03:00", token="BAD")
check("9. token invalido: error registrado, no publica", rc != 0 and not S["media"] and day(c, 8)["publish_status"] != "published")
# 10 dia futuro / atraso
reset(); d = mk(); rc, c = run(d, "2026-10-13T19:01:00-03:00")
check("10. 13/10 (antes del inicio) no publica", not S["media"])
rc, c = run(d, "2026-10-16T19:01:00-03:00")
check("10b. si se perdio un dia, publica el Dia 8 atrasado (no salta a 10)", day(c, 8)["publish_status"] == "published" and day(c, 10)["publish_status"] == "pending")
# 11 dry run real con los 5 videos
reset(); d = mk(); rc, c = run(d, "2026-10-14T19:01:00-03:00", extra=("--dry-run",))
check("11. dry-run valida video real (ffprobe) sin llamar a la API", rc == 0 and not S["media"] and day(c, 8)["publish_status"] == "pending")
# 12 todos los videos reales validan
sys.path.insert(0, REPO + "/autopost"); import publish
bad = [(x["day"], publish.validate_video(x)) for x in json.load(open(REPO + "/schedule.json"))["days"] if publish.validate_video(x)]
check(f"12. los 5 videos reales pasan la validacion {bad}", not bad)
print("FALLOS:", ok); sys.exit(1 if ok else 0)
