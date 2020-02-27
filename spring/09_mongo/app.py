# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template, request, session
from pymongo import MongoClient
# import pymongo

app = Flask(__name__)
f1 = open('primer-dataset.json', 'r')
client = MongoClient()
db = client['restaurants']

@app.route('/')
def main():
    return render_template(
            'foo.html'
            )

@app.route('/filter')
def filter():
    if request.method == "POST":
        borough = request.form['borough']
        zip = request.form['zip']
        grade = request.form['grade']
        score = request.form['score']

if __name__ == '__main__':
    app.debug = True
    app.run()
