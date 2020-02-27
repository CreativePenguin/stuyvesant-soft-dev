# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template, request, session
from pymongo import MongoClient
import pymongo

app = Flask(__name__)
f1 = open('primer-dataset.json', 'r')
client = MongoClient()
db = client['09_mongo']
restaurant = db['restaurants']
restaurant_id = restaurant.insert_one(f1).inserted_id()

@app.route('/')
def main():
    return render_template(
            'foo.html'
            )

@app.route('/filter')
def filter():
    if request.method == "POST":
        borough = request.form['borough']
        zipcode = request.form['zip']
        grade = request.form['grade']
        score = request.form['score']

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
