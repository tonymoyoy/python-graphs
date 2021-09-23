from flask import Flask
from flask.templating import render_template


app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")


if __name__ == "__main__":
    app.run(debug=True, port=5050, host="127.0.0.1")