# api/index.py
from http.server import BaseHTTPRequestHandler

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Happy Teacher's Day</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #f3f4f6;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
    }
    .card {
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.1);
      text-align: center;
      max-width: 400px;
    }
    h1 {
      color: #4f46e5;
      margin-bottom: 10px;
    }
    p {
      color: #374151;
      font-size: 16px;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>💝 Happy Teacher's Day ♥️</h1>
    <h2>To: Alvin</h2>
    <p>Thank you for inspiring me every day.<br>
    You are appreciated and celebrated!</p>
    <p style="margin-top:20px;">— Your student</p>
  </div>
</body>
</html>
"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))
