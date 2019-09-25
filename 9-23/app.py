# Winston Peng
# SoftDev1 pd9
# K
# 2019-9-23

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def main():
    print(app)
    print(request)
    print(request.args)
    return 'hello'
@app.route('/foo.html')
def blah():
    return render_template(
            'foo.html'
            )

if __name__ == '__main__':
    app.debug = True
    app.run()
