from flask import Flask

@app.route("/")
@app.route("/pengwin")
@app.route("/wpeng00")

def hello_world():
    print(__name__)
    return "No hablo queso!"

