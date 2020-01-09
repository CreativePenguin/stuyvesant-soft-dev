# Winston Peng
# SoftDev1 pd9
# K #24: A RESTful Journey Skyward
# 2019-9-23

from flask import Flask, render_template, request
import urllib3, json

app = Flask(__name__)
nasa_key = 'zUNNcvA48NgnrzwcdqBgI3YGKKFYgfwmVxDf0jHb'
http = urllib3.PoolManager()
httprequest = http.request('GET', 'https://api.nasa.gov/planetary/apod?{}{}'.format('api_key=', nasa_key))
http_dict = json.loads(httprequest.data.decode('utf-8'))


@app.route('/')
def main():
    return render_template(
        'index.html',
        tmp=httprequest,
        ext=http_dict['explanation']
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
