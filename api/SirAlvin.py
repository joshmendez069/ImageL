# api/josh.py
from http.server import BaseHTTPRequestHandler

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8"/>
  <title>Suprise: >>></title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #133337;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      margin: 0;
      color: #333;
    }
    .card {
      background: #fff;
      padding: 30px;
      border-radius: 12px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.2);
      text-align: center;
      max-width: 420px;
      width: 100%;
    }
    h1 {
      color: #4f46e5;
      margin-bottom: 10px;
    }
    p {
      font-size: 16px;
    }
    .comment-box {
      margin-top: 20px;
      text-align: left;
    }
    input, textarea {
      width: 100%;
      padding: 8px;
      margin-bottom: 10px;
      border-radius: 6px;
      border: 1px solid #ccc;
      font-size: 14px;
    }
    button {
      background: #4f46e5;
      color: white;
      padding: 8px 14px;
      border: none;
      border-radius: 6px;
      cursor: pointer;
    }
    button:hover {
      background: #3730a3;
    }
    .comments-list {
      margin-top: 15px;
      background: #f9fafb;
      padding: 10px;
      border-radius: 8px;
      max-height: 150px;
      overflow-y: auto;
      font-size: 14px;
    }
    .comment {
      padding: 6px 0;
      border-bottom: 1px solid #e5e7eb;
    }
    .comment:last-child {
      border-bottom: none;
    }
    .comment strong {
      color: #111827;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>💝 Happy Teacher's Day ♥️</h1>
    <h2>Sir Alvin</h2>
    <p>Thank you po sa lahat ng effort nyo maturuan lang kami 😺.</p>
    <p style="margin-top:20px;">— Josh Pogi</p>

    <div class="comment-box">
      <h3>Leave a Comment</h3>
      <input id="nameInput" type="text" placeholder="Your name">
      <textarea id="commentInput" rows="3" placeholder="Write your comment..."></textarea>
      <button onclick="addComment()">Post Comment</button>

      <div class="comments-list" id="commentsList">
        <!-- Comments will show here -->
      </div>
    </div>
  </div>

  <script>
    function addComment() {
      const name = document.getElementById('nameInput').value.trim();
      const comment = document.getElementById('commentInput').value.trim();
      if (name === '' || comment === '') return;

      const list = document.getElementById('commentsList');
      const div = document.createElement('div');
      div.className = 'comment';
      div.innerHTML = '<strong>' + name + ':</strong> ' + comment;
      list.appendChild(div);

      // clear inputs
      document.getElementById('nameInput').value = '';
      document.getElementById('commentInput').value = '';
    }
  </script>
</body>
</html>
"""

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode("utf-8"))
