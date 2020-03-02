import pymongo
import bson.json_util
from pprint import pprint

client = pymongo.MongoClient('localhost', 27017)
db = client['09_mongo']
restaurant = db['restaurants']

def fill_database():
    with open('primer-dataset.json') as f:
        for line in f.readlines():
            restaurant.insert_one(bson.json_util.loads(line))

def cleanse(borough=None, zipcode=None, grade=None, score=None):
    filter_params = {}
    if not zipcode is None:
        filter_params['address'] = {}
        filter_params['address']['zipcode'] = zipcode
    if not grade is None or not score is None:
        filter_params['date'] = {}
    if not borough is None:
        filter_params['borough'] = borough
    if not grade is None:
        filter_params['date']['grade'] = grade
    if not score is None:
        filter_params['date']['score'] = score
    # filter_params = {}
    # filter_params['address'] = {}
    # filter_params['address']['zipcode'] = zipcode
    # filter_params['date'] = {}
    # filter_params['borough'] = borough
    # filter_params['date']['grade'] = grade
    # filter_params['date']['score'] = score
    return filter_params

# fill_database()
# for col in restaurant.find({}):
#     pprint(col)
print(cleanse(borough='Queens'))
for line in restaurant.find(cleanse(borough='Queens'), {'_id': 0, 'name': 1, 'borough': 1}):
    pprint(line)
# pprint(restaurant.find_one(cleanse(borough='Queens'), {'_id': 0, 'name': 1, 'borough': 1}))
