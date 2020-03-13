# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template
import urllib.request
import json
import utl.funcs
import bson.json_util
import pymongo

app = Flask(__name__)

@app.route('/')
def main():
    return render_template(
        'foo.html'
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
