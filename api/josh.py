# api/index.py
from http.server import BaseHTTPRequestHandler

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>Teacher's Day — Simple (Python on Vercel)</title>
  <style>
    :root{--bg:#f8fafc;--card:#fff;--accent:#6366f1}
    body{font-family:system-ui,Segoe UI,Roboto,Arial;margin:0;background:linear-gradient(180deg,var(--bg),#fff);min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px;}
    .wrap{max-width:980px;width:100%;display:grid;grid-template-columns:1fr 1fr;gap:20px}
    .panel{background:var(--card);padding:20px;border-radius:12px;box-shadow:0 8px 30px rgba(2,6,23,0.08)}
    h1{margin:0 0 8px;font-size:20px}
    label{display:block;margin-top:12px;font-weight:600;font-size:13px}
    input,textarea{width:100%;padding:8px;border-radius:8px;border:1px solid #e6e9ef;margin-top:6px;font-size:14px}
    .row{display:flex;gap:8px;margin-top:12px}
    button{padding:10px 14px;border-radius:10px;border:0;cursor:pointer;font-weight:700}
    .primary{background:var(--accent);color:#fff}
    .muted{background:#f1f5f9}
    /* preview */
    .card{border-radius:12px;overflow:hidden;width:100%;max-width:460px}
    .card .head{padding:20px;background:linear-gradient(90deg,var(--accent),#4f46e5);color:#fff}
    .card .head .title{font-size:20px;margin:0}
    .card .body{background:#fff;padding:18px;color:#0f172a}
    .small{font-size:13px;color:#6b7280;margin-top:12px}
    footer.small{margin-top:14px;text-align:center;color:#94a3b8;font-size:13px}
    @media (max-width:800px){.wrap{grid-template-columns:1fr;}}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="panel">
      <h1>Teacher's Day — Simple</h1>
      <label>Teacher's name</label>
      <input id="teacher" value="Dear Teacher" />
      <label>Message</label>
      <textarea id="message" rows="5">Thank you for inspiring me every day.</textarea>
      <label>Emoji</label>
      <input id="emoji" value="🌟" />
      <div class="row">
        <button class="primary" onclick="updateCard()">Update</button>
        <button class="muted" onclick="resetCard()">Reset</button>
      </div>
      <div class="small">This page is served by a Python function on Vercel.</div>
    </div>

    <div class="panel" style="display:flex;align-items:center;justify-content:center;flex-direction:column;">
      <div class="card" id="preview">
        <div class="head">
          <div class="title"><span id="emojiPreview">🌟</span> Teacher's Day</div>
          <div id="teacherPreview" style="opacity:0.9;margin-top:6px;font-weight:600">Dear Teacher</div>
        </div>
        <div class="body">
          <div id="messagePreview">Thank you for inspiring me every day.</div>
          <div class="small">— Your student</div>
        </div>
      </div>
      <footer class="small">Made with ❤️</footer>
    </div>
  </div>

  <script>
    function updateCard(){
      document.getElementById('teacherPreview').textContent = document.getElementById('teacher').value || 'Dear Teacher';
      document.getElementById('messagePreview').textContent = document.getElementById('message').value || '';
      document.getElementById('emojiPreview').textContent = document.getElementById('emoji').value || '🌟';
    }
    function resetCard(){
      document.getElementById('teacher').value = 'Dear Teacher';
      document.getElementById('message').value = 'Thank you for inspiring me every day.';
      document.getElementById('emoji').value = '🌟';
      updateCard();
    }
    window.addEventListener('DOMContentLoaded', updateCard);
  </script>
</body>
</html>
"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve the HTML page for any GET request
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))
