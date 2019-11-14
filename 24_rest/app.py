# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template, request
import urllib3, json

app = Flask(__name__)
nasa_key = 'zUNNcvA48NgnrzwcdqBgI3YGKKFYgfwmVxDf0jHb'
http = urllib3.PoolManager()

@app.route('/')
def main():
    return render_template(
        'index.html',
        tmp=http.request('GET', 'https://api.nasa.gov/planetary/apod?={}'.format(nasa_key))
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
