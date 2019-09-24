# Winston Peng
# SoftDev1 pd9
# K10 -- Jinja Tuning
# 2019-9-23

from flask import Flask, render_template
import static.script as script

app = Flask(__name__)

@app.route('/occupyflaskst')
def occupations():
    return render_template(
            'occ.html',
            team = 'Connor Oh, Nahi Khan, Winston Peng -- Team Beaker',
            header = 'Jinja Tuning -- Occupations',
            title = 'Job Occupations',
            randOcc = script.sol(),
            occ = script.arr()
            )

if __name__ == '__main__':
    app.debug = True
    app.run()

