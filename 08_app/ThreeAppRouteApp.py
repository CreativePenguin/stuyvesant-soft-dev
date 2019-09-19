from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/pengwin")
@app.route("/wpeng00")

def hello_world():
    print(__name__)
    return "No hablo queso!"

