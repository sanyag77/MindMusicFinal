from flask import Flask, render_template_string, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def index():
    return render_template('audio.html')

if __name__ == "__main__":
    app.run(debug=True, threaded=True)

#video: https://www.youtube.com/watch?v=vuaolF-OSGY

# @app.route("/", methods=["GET", "POST"])
# def index():
#     return "hello world"
#     #return render_template('html/audio.html')
# if __name__ == "__main__":
#      app.run(debug=True, threaded=True)