from flask import Flask
from flask import request
from flask import Response
from RobieLegs import *

app = Flask(__name__)


@app.route('/robie/legs', methods=['POST'])
def api_Legs():

    if request.headers['Content-Type'] == 'application/json':
        x = request.json['x']
        y = request.json['y']
        RobieLegs().roll(x, y)
        resp = Response()
        resp.status_code = 200
        resp.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp
