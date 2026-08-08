"""Phone -> PC trigger for the YouTube pipelines.

A tiny, token-protected HTTP server. Open it from your phone (over Tailscale) to:
  - generate a DRAFT ranking Short (Ranked Chaos) from a topic you type,
  - trigger the kick pipeline's n8n auto-upload (uploads land PRIVATE),
  - see recent renders + job status.

Honest scope: the PC does the rendering (phone can't). Generated Shorts are DRAFTS
- review them before publishing. Kick GENERATION still needs a Claude session; only
kick UPLOAD is a webhook, so that's what's exposed here.

Run (PC must stay on):
    python "T:\Youtube CEO\mobile_trigger\mobile_trigger.py"
Then from your phone (same Tailscale network):
    http://<pc-tailscale-ip>:8799/?k=<token>
"""
import json
import os
import subprocess
import threading
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

BASE = os.path.dirname(os.path.abspath(__file__))
RANK_DIR = r"T:\Youtube Shorts 2\ranking_pipeline"
OUT_DIR = r"T:\Youtube Shorts 2"
LOGS = os.path.join(BASE, "logs")
TOKEN = open(os.path.join(BASE, "token.txt"), encoding="utf-8").read().strip()
PORT = 8799
N8N_UPLOAD_WEBHOOK = "http://localhost:5678/webhook/run-upload"

os.makedirs(LOGS, exist_ok=True)
JOBS = {}   # job_id -> {"status","started","cmd","log"}


def slug(s):
    import re
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")[:60] or "topic"


def _run(job_id, steps, cwd):
    """Run a list of (label, argv) steps, logging to logs/<job_id>.log."""
    logf = os.path.join(LOGS, f"{job_id}.log")
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    JOBS[job_id]["status"] = "running"
    with open(logf, "w", encoding="utf-8") as lf:
        for label, argv in steps:
            lf.write(f"\n=== {label} ===\n{' '.join(argv)}\n"); lf.flush()
            try:
                p = subprocess.run(argv, cwd=cwd, env=env, capture_output=True,
                                   text=True, encoding="utf-8", errors="replace",
                                   timeout=1800)
                lf.write((p.stdout or "")[-4000:]); lf.write((p.stderr or "")[-2000:])
                lf.flush()
                if p.returncode != 0:
                    JOBS[job_id]["status"] = f"failed at: {label}"
                    return
            except Exception as e:
                lf.write(f"\nERROR: {e}\n")
                JOBS[job_id]["status"] = f"error: {e}"
                return
    JOBS[job_id]["status"] = "done"


def start_ranking(topic):
    s = slug(topic)
    job_id = f"rank_{s}_{int(time.time())}"
    pool = os.path.join("_cache", f"{s}_mob.tsv")
    steps = [
        ("source (US-filtered, no Indian)",
         ["python", "source_clips.py", topic, pool]),
        ("render draft",
         ["python", "make_short.py", topic, "--want", "6",
          "--urls-file", pool, "--max-total", "46"]),
    ]
    JOBS[job_id] = {"status": "queued", "started": time.strftime("%H:%M:%S"),
                    "cmd": f"ranking: {topic}"}
    threading.Thread(target=_run, args=(job_id, steps, RANK_DIR), daemon=True).start()
    return job_id


def kick_upload():
    try:
        req = urllib.request.Request(N8N_UPLOAD_WEBHOOK, method="POST", data=b"{}")
        with urllib.request.urlopen(req, timeout=20) as r:
            return True, r.read().decode("utf-8", "replace")[:300]
    except Exception as e:
        return False, str(e)


def recent_mp4s(n=8):
    try:
        fs = [(f, os.path.getmtime(os.path.join(OUT_DIR, f)))
              for f in os.listdir(OUT_DIR) if f.lower().endswith(".mp4")]
        fs.sort(key=lambda x: -x[1])
        return [f for f, _ in fs[:n]]
    except Exception:
        return []


PAGE = """<!doctype html><html><head><meta name=viewport content="width=device-width,initial-scale=1">
<title>YT CEO Trigger</title><style>
body{{font-family:system-ui;background:#0b0f19;color:#e6edf3;margin:0;padding:18px;max-width:640px}}
h1{{font-size:20px}} .card{{background:#161b26;border:1px solid #232a37;border-radius:14px;padding:16px;margin:12px 0}}
input,button{{font-size:17px;border-radius:10px;border:1px solid #2a3342;padding:12px;width:100%;box-sizing:border-box}}
input{{background:#0d1117;color:#e6edf3;margin-bottom:10px}}
button{{background:#2f81f7;color:#fff;border:none;font-weight:600;margin-top:6px}}
button.gray{{background:#30363d}} .s{{color:#9aa4b2;font-size:13px}} a{{color:#58a6ff}}
pre{{white-space:pre-wrap;word-break:break-word;background:#0d1117;padding:10px;border-radius:8px;font-size:12px}}
</style></head><body>
<h1>🎬 YouTube CEO — Mobile Trigger</h1>
<div class=card><b>Make a ranking short (draft)</b>
<p class=s>Type an oddly-specific topic. Sources US clips (no Indian), renders a draft to review.</p>
<input id=topic placeholder="e.g. Funniest Water Slide Fails">
<button onclick="go()">Generate draft</button></div>
<div class=card><b>Kick upload (Mr.GHCLIPS)</b>
<p class=s>Uploads rendered kick Shorts to YouTube as PRIVATE. Publish from the YouTube app.</p>
<button class=gray onclick="kick()">Run kick upload now</button></div>
<div class=card><b>Status</b> <button class=gray onclick="stat()">Refresh</button>
<pre id=out>tap refresh…</pre></div>
<script>
const K=new URLSearchParams(location.search).get('k')||'';
function j(u){{return fetch(u).then(r=>r.json())}}
function go(){{const t=document.getElementById('topic').value.trim();if(!t)return;
 j('/make-ranking?k='+K+'&topic='+encodeURIComponent(t)).then(d=>{{document.getElementById('out').textContent='started: '+d.job;stat()}})}}
function kick(){{j('/kick-upload?k='+K).then(d=>{{document.getElementById('out').textContent=JSON.stringify(d,null,1)}})}}
function stat(){{j('/status?k='+K).then(d=>{{document.getElementById('out').textContent=JSON.stringify(d,null,1)}})}}
stat();
</script></body></html>"""


class H(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype="application/json"):
        b = body.encode("utf-8") if isinstance(body, str) else body
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(b))); self.end_headers()
        self.wfile.write(b)

    def _auth(self, q):
        return q.get("k", [""])[0] == TOKEN

    def log_message(self, *a):  # quiet
        pass

    def do_GET(self):
        u = urlparse(self.path); q = parse_qs(u.query)
        if u.path == "/" :
            if not self._auth(q):
                return self._send(401, "unauthorized (add ?k=TOKEN)", "text/plain")
            return self._send(200, PAGE, "text/html")
        if not self._auth(q):
            return self._send(401, json.dumps({"error": "unauthorized"}))
        if u.path == "/make-ranking":
            topic = (q.get("topic", [""])[0] or "").strip()
            if not topic:
                return self._send(400, json.dumps({"error": "topic required"}))
            return self._send(200, json.dumps({"job": start_ranking(topic)}))
        if u.path == "/kick-upload":
            ok, msg = kick_upload()
            return self._send(200, json.dumps({"ok": ok, "msg": msg}))
        if u.path == "/status":
            return self._send(200, json.dumps({
                "jobs": {k: v["status"] for k, v in sorted(JOBS.items())[-8:]},
                "recent_mp4s": recent_mp4s()}, indent=1))
        return self._send(404, json.dumps({"error": "not found"}))

    do_POST = do_GET


if __name__ == "__main__":
    print(f"Mobile trigger on http://0.0.0.0:{PORT}  (token in token.txt)")
    print(f"Local test: http://localhost:{PORT}/?k={TOKEN}")
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()
