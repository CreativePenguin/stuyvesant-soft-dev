# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template, request, session
import filter_restaurants

app = Flask(__name__)
# f1 = open('primer-dataset.json', 'r')
# json.load(f1.readlines())
# f1.close()
# with open('primer-dataset.json') as f:
#     filedata = json.load(f)
# restaurant_id = restaurant.insert_one(filedata).inserted_id()

if filter_restaurats.restaurant.find({}) is None:
    filter_restaurants.fill_databse()


@app.route('/')
def main():
    # Next line should return session['filtered_data'] only if it's not None
    restaurant_info = \
    filter_restaurants.restaurant.find(session['restaurant_data'],
        {'_id': 0}) or filter_restaurants.restaurant.find({},
        {'_id': 0})
    return render_template(
        'foo.html',
        data=restaurant_info
    )


@app.route('/filter')
def restaurant_filter():
    if request.method == "POST":
        session['restaurant_data'] = filter_restaurants.restaurant.find(
            filter_restaurants.cleanse(
                request.form['borough'],
                request.form['zip'],
                request.form['grade'],
                request.form['score']
            ), {'_id': 0})
        # session['filtered_data'] = restaurant_id.find(filter_params, {'_id': 0})


client.close()

if __name__ == '__main__':
    app.debug = True
    app.run()
