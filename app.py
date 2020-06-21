from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello This is my flask application"


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')
