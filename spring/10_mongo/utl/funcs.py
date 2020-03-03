import urllib.request
import json
import pymongo
import bson.json_util
from pprint import pprint


client = pymongo.MongoClient('localhost', 27017)
db = client['10_mongo']
senators = db['senators']

def fill_database():
    u = urllib.request.urlopen('https://www.govtrack.us/api/v2/role?current=true&role_type=senator')
    response = u.read()
    data = json.loads(reponse)
    senators.insert_one(json_util.loads(line))

if senators.find({}) is None:
    fill_database()

print(senators.find({}))
