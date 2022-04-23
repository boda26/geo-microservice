#
from datetime import datetime
import os
from flask.wrappers import Response
import requests
import json
# export FLASK_APP=IM_state

from flask import Flask, render_template, request, jsonify

im_ip = os.getenv('IM_IP')
app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    # local_ip = os.getenv('LOCAL_IP')
    im_ip = os.getenv('IM_IP')

    # http://127.0.0.1:5000/microservice
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5002',
        'ip': 'http://172.22.150.47',
        'name': 'City',
        'creator': 'Harry Xia',
        'tile': 'City',
        'dependencies': []
    })
    return 'IM_city added!',200


@app.route('/delete', methods=['GET'])
def delete():
    # local_ip = os.getenv('LOCAL_IP')

    # http://127.0.0.1:5000/microservice
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5002',
        'ip': 'http://172.22.150.47'
    })
    return 'IM_city deleted!', 200


@app.route('/', methods=["GET"])
def get_location():
    input = request.data.decode('utf-8')
    input_json = json.loads(input)
    lat = str(input_json['latitude'])
    lon = str(input_json['longitude'])
    key = lat + ',' + lon

    weather_url = 'https://api.weather.gov/points'
    r = requests.get(f'{weather_url}/{key}')
    js = r.json()
    if ('correlationId' in js):
        json_response = jsonify(
            errorMessage = 'Invalid geographical location!',
        )
        now = datetime.now().timestamp()
        json_response.age = int(now)
        json_response.cache_control.max_age = int(now) + 1800
        return json_response

    lat = js["properties"]["relativeLocation"]["geometry"]["coordinates"][1]
    lon = js["properties"]["relativeLocation"]["geometry"]["coordinates"][0]
    city = js["properties"]["relativeLocation"]["properties"]["city"]

    json_response = jsonify(
        lat = lat,
        lon = lon, 
        city = city
    )
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 1800
    #print(json_response.headers)
    return json_response