# export FLASK_APP=IM_city
import os
import requests
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/add', methods=['GET','PUT'])
def add():
    # local_ip = os.getenv('LOCAL_IP')
    im_ip = 'http://172.22.150.47'
    # http://127.0.0.1:5000/microservice
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5001',
        'ip': im_ip,
        'name': 'State',
        'creator': 'Boda Song',
        'tile': 'State',
        'dependencies': []
    })
    return 'IM_state added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    # local_ip = os.getenv('LOCAL_IP')
    im_ip = 'http://172.22.150.47'

    # http://127.0.0.1:5000/microservice
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5001',
        'ip': im_ip
    })
    return 'IM_state deleted!', 200


@app.route('/', methods=['GET'])
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

    state = js["properties"]["relativeLocation"]["properties"]["state"]
    json_response = jsonify(
        state = state
    )
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 1800
    return json_response