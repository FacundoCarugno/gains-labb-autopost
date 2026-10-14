"""Cliente minimo de la API oficial de Instagram (Instagram Login, graph.instagram.com). Solo biblioteca estandar."""
import json, os, urllib.request, urllib.parse, urllib.error

class ApiError(Exception):
    def __init__(self, msg, status=None, body=None):
        super().__init__(msg); self.status = status; self.body = body

class IG:
    def __init__(self, token, ig_id, base=None, version="v23.0"):
        self.token, self.ig_id = token, ig_id
        self.base = (base or os.environ.get("IG_API_BASE") or "https://graph.instagram.com").rstrip("/") + "/" + version

    def _call(self, method, path, params=None):
        params = dict(params or {}); params["access_token"] = self.token
        url = f"{self.base}/{path.lstrip('/')}"
        data = None
        if method == "GET":
            url += "?" + urllib.parse.urlencode(params)
        else:
            data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(url, data=data, method=method)
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode() or "{}")
        except urllib.error.HTTPError as e:
            body = e.read().decode(errors="replace")
            raise ApiError(f"HTTP {e.code} en {method} {path}: {body[:400]}", e.code, body)
        except urllib.error.URLError as e:
            raise ApiError(f"Red: {e.reason} en {method} {path}")

    def whoami(self):               return self._call("GET", "me", {"fields": "user_id,username,account_type"})
    def create_reel(self, video_url, caption, share_to_feed=True):
        return self._call("POST", f"{self.ig_id}/media", {"media_type": "REELS", "video_url": video_url,
                          "caption": caption, "share_to_feed": "true" if share_to_feed else "false"})["id"]
    def container_status(self, cid):  return self._call("GET", cid, {"fields": "status_code,status"})
    def publish(self, cid):           return self._call("POST", f"{self.ig_id}/media_publish", {"creation_id": cid})["id"]
    def recent_media(self, n=25):     return self._call("GET", f"{self.ig_id}/media", {"fields": "id,caption,media_product_type,timestamp,permalink", "limit": n}).get("data", [])
    def comment(self, media_id, text): return self._call("POST", f"{media_id}/comments", {"message": text})["id"]
    def refresh_token(self):          return self._call("GET", "refresh_access_token", {"grant_type": "ig_refresh_token"})
