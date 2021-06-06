from flask import render_template, request, Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route("/", methods=['GET', 'POST'])
def home():
    # year = datetime.datetime.now().year
    return render_template('index.hItml')


if __name__ == '__main__':
    app.run(debug=True)
