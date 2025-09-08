from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>Teacher's Day Letter</title>
      <style>
        body {
          margin: 0;
          height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          background: #133337;
          font-family: Arial, sans-serif;
        }

        .envelope {
          position: relative;
          width: 300px;
          height: 200px;
          background: #e0c097;
          border-radius: 6px;
          overflow: hidden;
          cursor: pointer;
        }

        .flap {
          position: absolute;
          top: 0;
          left: 0;
          width: 100%;
          height: 100%;
          background: #d4a373;
          clip-path: polygon(0 0, 100% 0, 50% 50%);
          transform-origin: top;
          transition: transform 1s ease;
        }

        .letter {
          position: absolute;
          bottom: -100%;
          left: 0;
          width: 100%;
          height: 100%;
          background: #fff;
          text-align: center;
          padding: 20px;
          box-sizing: border-box;
          transition: bottom 1s ease;
        }

        .letter h1 {
          color: #4f46e5;
          margin: 0;
        }

        .letter p {
          color: #374151;
          font-size: 16px;
        }

        .envelope.open .flap {
          transform: rotateX(180deg);
        }

        .envelope.open .letter {
          bottom: 0;
        }
      </style>
    </head>
    <body>
      <div class="envelope" onclick="this.classList.toggle('open')">
        <div class="flap"></div>
        <div class="letter">
          <h1>💝 Happy Teacher's Day 💝</h1>
          <p>Thank you so much Sir Alvin<br>
          for guiding and teaching us always! 😺</p>
          <p style="margin-top:15px;">— Josh Pogi</p>
        </div>
      </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
