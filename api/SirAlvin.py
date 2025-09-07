from flask import Flask, request, render_template_string, redirect
import os
import redis

app = Flask(__name__)

# Connect to Redis using REDIS_URL from Vercel
redis_url = os.getenv("Josh")
r = redis.from_url(redis_url)

# HTML Template
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Happy Teacher's Day!</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f0f8ff; text-align: center; padding: 20px; }
        h1 { color: #2c3e50; }
        form { margin: 20px auto; max-width: 400px; }
        input[type=text] { width: 80%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; background: #2c3e50; color: white; border: none; border-radius: 5px; cursor: pointer; }
        button:hover { background: #34495e; }
        .comment-box { background: white; border: 1px solid #ddd; margin: 10px auto; padding: 10px; max-width: 400px; border-radius: 5px; }
    </style>
</head>
<body>
    <h1>🎉 Happy Teacher's Day Alvin! 🎉</h1>
    <p>Thank you for your guidance and wisdom. 💙</p>

    <h2>Leave a Comment</h2>
    <form method="POST" action="/add_comment">
        <input type="text" name="comment" placeholder="Write your comment..." required>
        <button type="submit">Post</button>
    </form>

    <h2>Comments</h2>
    {% for c in comments %}
        <div class="comment-box">{{ c }}</div>
    {% else %}
        <p>No comments yet. Be the first!</p>
    {% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    comments = r.lrange("comments", 0, -1)  # Get all comments
    comments = [c.decode("utf-8") for c in comments]  # Convert from bytes
    return render_template_string(HTML, comments=comments)

@app.route("/add_comment", methods=["POST"])
def add_comment():
    comment = request.form.get("comment")
    if comment:
        r.rpush("comments", comment)  # Save to Redis list
    return redirect("/")
