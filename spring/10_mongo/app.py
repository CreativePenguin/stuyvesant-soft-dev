# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask, render_template, request
import urllib, json

app = Flask(__name__)
u = urllib.request.urlopen('https://www.govtrack.us/api/v2/role?current=true&role_type=senator')
response = u.read()
data = json.loads(reponse)

@app.route('/')
def main():
    return render_template(
        'foo.html'
    )

if __name__ == '__main__':
    app.debug = True
    app.run()
