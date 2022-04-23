import os
import requests
from datetime import datetime
import json
# export FLASK_APP=IM_state

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

im_ip = 'http://172.22.150.47'

@app.route('/add', methods=['GET','PUT'])
def add():
    # local_ip = os.getenv('LOCAL_IP')
    # http://127.0.0.1:5000/microservice
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5006',
        'ip': im_ip,
        'name': 'Timezone',
        'creator': 'Harry Xia',
        'tile': 'Timezone',
        'dependencies': []
    })
    return 'IM_elevation added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    # local_ip = os.getenv('LOCAL_IP')
    # http://127.0.0.1:5000/microservice
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5006',
        'ip': im_ip
    })
    return 'IM_elevation deleted!', 200


@app.route('/', methods=["POST","GET"])
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

    timeZone = js["properties"]["timeZone"]
    json_response = jsonify(
        timeZone = timeZone
    ) 
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 1800
    return json_response