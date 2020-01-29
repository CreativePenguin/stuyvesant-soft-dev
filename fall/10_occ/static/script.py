#Winston Peng
#SoftDev1 pd9
#K06 -- Divine your Destiny!
#2019-09-17

import csv
import random

# Change based on where you run this file
# If called from app.py, will use second one
try:
    file = open('occupations.csv', 'r')
except FileNotFoundError:
    file = open('static/occupations.csv', 'r')
readfile = file.readlines()

def csvToDict(csv, dic={}):
    if csv:
        # arr = list. arr[0] = occupation. arr[1] = percentage
        arr = csv.pop(0).rstrip('\n').rsplit(',', 1)
        # transform array indexes to key and value in dictionary
        dic[arr[0]] = arr[1]
        return csvToDict(csv, dic)
    return dic

csvDict = csvToDict(readfile)
# calcs rand num, and then subtracts the various values, until one brings it under 0
def randJob(dic=csvDict):
    rand = random.randint(0, 99)
    for i in list(dic.keys())[1:]:
        rand -= float(dic[i])
        if rand < 0:
            return i
    raise Exception('Either you\'re really bad at math, or code is broke')

'''
def sol():
    dictionary = {}
    total = 0;
    for line in readfile:
        idx = line.rfind(",")
        job = line[:idx]
        percent = float(line[idx+1:-1])
        dictionary[job] = round(percent + total,1)
        total += percent
    del dictionary["Total"]
    rand = random.randint(1,998) * 0.1
    for key in dictionary.keys():
        if rand <= dictionary[key]:
            return key
'''    

