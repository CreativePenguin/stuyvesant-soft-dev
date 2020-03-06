import urllib.request
import pymongo
import bson.json_util
import pprint as pp
import json
from pprint import pprint


client = pymongo.MongoClient('localhost', 27017)
db = client['10_mongo']
senators = db['senators']

def fill_database():
    response = urllib.request.urlopen(
        'https://www.govtrack.us/api/v2/role?current=true&role_type=senator')\
                             .read()
    data = json.loads(response)['objects']
    json_data = json.dumps(data)
    senators.delete_one(data[0])
    for senator in data:
        senators.insert_one(senator)
    # bson_data = bson.json_util.loads(json_data)
    # senators.insert_one(bson.json_util.loads(json_data))

def is_empty_database(db):
    try:
        db.find({})[0]
    except IndexError:
        return True
    return False

def print_database(db, filter_params={}, print_params={'_id': 0,
                                                       'caucus': 0,
                                                       'title': 0,
                                                       'title_long': 0}):
    for line in db.find(filter_params, print_params):
        print(line)

def cleanse(party=None, gender=None, senator_rank=None):
    filter_params = {}
    if not gender is None:
        filter_params['person'] = {}
        filter_params['person']['gender'] = gender
    if not senator_rank is None:
        filter_params['senator_rank'] = senator_rank
    if not party is None:
        filter_params['party'] = party
    return filter_params

if is_empty_database(senators):
    fill_database()
print_database(senators, {'website': 'https://www.coons.senate.gov'})
# print_database(senators)
