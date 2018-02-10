from flask import Flask
from flask import request
from flask import Response
from flask.ext.cors import CORS, cross_origin
from RobieLegs import *
from RobieEyes import *

app = Flask(__name__)

cors = CORS(app, resources={"/robie/legs": {"origins": "http://192.168.1.172:80"}})


@app.route('/robie/legs', methods=['POST'])
@cross_origin(origin='192.168.1.172', headers=['Content- Type', 'Authorization'])
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


@app.route('/robie/eyes', methods=['POST'])
@cross_origin(origin='192.168.1.172', headers=['Content- Type', 'Authorization'])
def api_Eyes():

    if request.headers['Content-Type'] == 'application/json':
        channel = request.json['eye']
        red = request.json['red']
        green = request.json['green']
        blue = request.json[' blue']
        RobieEyes().setColor(channel, red, green, blue)
        resp = Response()
        resp.status_code = 200
        response.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp


@app.route('/robie/eyes/close', methods=['POST'])
@cross_origin(origin='192.168.1.172', headers=['Content- Type', 'Authorization'])
def api_Eyes_Close():

    if request.headers['Content-Type'] == 'application/json':
        RobieEyes().blankEyes()
        resp = Response()
        resp.status_code = 200
        response.headers['server'] = ""
        return resp

    else:
        resp = Response("Try Again :-(", status=415, mimetype='text/plain')
        resp.headers['server'] = ""
        return resp
