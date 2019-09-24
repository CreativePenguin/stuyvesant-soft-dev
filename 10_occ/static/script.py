#Winston Peng
#SoftDev1 pd9
#K06 -- Divine your Destiny!
#2019-09-17

import csv
import random

try:
    file = open('occupations.csv', 'r')
except FileNotFoundError:
    file = open('static/occupations.csv', 'r')
readfile = file.readlines()

def arr():
    ans = []
    for line in readfile:
        ans.append(line.rstrip('\n').split(","))
    return ans

readfile.pop(0)

def sol():
    dictionary = {}
    total = 0;
    for line in readfile:
        idx = line.rfind(",")
        job = line[0:idx]
        percent = float(line[idx+1:-1])
        dictionary[job] = round(percent + total,1);
        total += percent
    del dictionary["Total"]
    rand = random.randint(1,998) * 0.1
    for key in dictionary.keys():
        if rand <= dictionary[key]:
            return key;

