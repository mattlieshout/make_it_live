from flask import render_template, request, Flask
import os

port = int(os.environ.get("PORT", 5000))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route("/")
def home():
    # year = datetime.datetime.now().year
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=port)
