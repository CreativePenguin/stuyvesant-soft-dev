# Winston Peng
# SoftDev1 pd9
# K10 -- Jinja Tuning
# 2019-9-23

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/occupyflaskst')
def occupations():
    return render_template(
            'occ.html',
            team = 'beaker',
            header = 'Jinja Tuning -- Occupations',
            title = 'Job Occupations'
            )

