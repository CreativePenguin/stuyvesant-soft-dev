# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template, request, session
from pymongo import MongoClient
import pymongo
import json

app = Flask(__name__)
client = MongoClient()
db = client['09_mongo']
restaurant = db['restaurants']
# f1 = open('primer-dataset.json', 'r')
# json.load(f1.readlines())
# f1.close()
with open('primer-dataset.json') as f:
    filedata = json.load(f)
restaurant_id = restaurant.insert_one(filedata).inserted_id()


@app.route('/')
def main():
    print(restaurant_id.find({}, {'_id': 0}))
    restaurant_info = restaurant_id.find({}, {'_id': 0})
    return render_template(
        'foo.html',
        data=restaurant_info
    )

@app.route('/filter')
def filter():
    if request.method == "POST":
        filter_params = {}
        zipcode = request.form['zip']
        grade = request.form['grade']
        score = request.form['score']
        if not request.form['borough'] is None:
            filter_params['borough'] = borough

client.close()
if __name__ == '__main__':
    app.debug = True
    app.run()
