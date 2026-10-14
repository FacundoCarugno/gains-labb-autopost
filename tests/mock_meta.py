"""Servidor Meta simulado (solo para pruebas locales; no toca Instagram)."""
import json, sys, threading, urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
S = {"containers": {}, "media": [], "comments": [], "fail_publish_once": False, "crash_after_publish": False, "n": 0, "calls": []}
class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _send(self, code, obj, ctype="application/json"):
        b = json.dumps(obj).encode(); self.send_response(code); self.send_header("Content-Type", ctype); self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b)
    def do_HEAD(self):
        self.send_response(200); self.send_header("Content-Type", "video/mp4"); self.end_headers()
    def _p(self):
        u = urllib.parse.urlparse(self.path); q = dict(urllib.parse.parse_qsl(u.query))
        n = int(self.headers.get("Content-Length") or 0)
        if n: q.update(dict(urllib.parse.parse_qsl(self.rfile.read(n).decode())))
        return u.path.split("/", 2)[2], q   # quita /v23.0
    def do_GET(self):
        p, q = self._p(); S["calls"].append(("GET", p))
        if q.get("access_token") != "GOOD": return self._send(400, {"error": {"message": "Invalid OAuth access token", "code": 190}})
        if p == "me": return self._send(200, {"user_id": "123", "username": "gains.labb"})
        if p == "123/media": return self._send(200, {"data": S["media"]})
        if p in S["containers"]: return self._send(200, {"status_code": S["containers"][p]["status"]})
        self._send(404, {"error": {"message": "not found"}})
    def do_POST(self):
        p, q = self._p(); S["calls"].append(("POST", p))
        if q.get("access_token") != "GOOD": return self._send(400, {"error": {"message": "Invalid OAuth access token", "code": 190}})
        if p == "123/media":
            S["n"] += 1; cid = f"c{S['n']}"; S["containers"][cid] = {"caption": q["caption"], "status": "FINISHED", "video_url": q["video_url"]}
            return self._send(200, {"id": cid})
        if p == "123/media_publish":
            if S["fail_publish_once"]: S["fail_publish_once"] = False; return self._send(500, {"error": {"message": "temporary"}})
            c = S["containers"][q["creation_id"]]; mid = "m" + q["creation_id"]
            S["media"].insert(0, {"id": mid, "caption": c["caption"], "media_product_type": "REELS"})
            if S["crash_after_publish"]: S["crash_after_publish"] = False; self.connection.close(); return
            return self._send(200, {"id": mid})
        if p.endswith("/comments"):
            S["comments"].append((p.split("/")[0], q["message"])); return self._send(200, {"id": "cm" + str(len(S["comments"]))})
        self._send(404, {"error": {"message": "not found"}})
    # control
    def do_PUT(self):
        n = int(self.headers.get("Content-Length") or 0); S.update(json.loads(self.rfile.read(n) or "{}")) if n else None
        self._send(200, {k: v for k, v in S.items() if k != "calls"})
def serve(port):
    srv = ThreadingHTTPServer(("127.0.0.1", port), H); threading.Thread(target=srv.serve_forever, daemon=True).start(); return srv
if __name__ == "__main__":
    serve(int(sys.argv[1])); import time; time.sleep(3600)
