# Winston Peng
# SoftDev1 pd 9
# K08 -- Lemme Flask You Sump'n
# 2019-09-19

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "This is the beginning of the page"
@app.route("/link")
def triforce():
    return 'woah look it\'s zelda'
@app.route("/creedthoughts")
def parks_and_rec():
    return 'How do you do fellow kids?'
if __name__ == '__main__': # Determines if file is being run by itself
    app.debug = True
    app.run()

