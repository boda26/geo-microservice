import os
import requests
from datetime import datetime
# export FLASK_APP=IM_state

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

im_ip = 'http://172.22.150.47'

@app.route('/add', methods=['GET','PUT'])
def add():
    # local_ip = os.getenv('LOCAL_IP')
    # http://127.0.0.1:5000/microservice
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5004',
        'ip': im_ip,
        'name': 'Elevation',
        'creator': 'Boda Song',
        'tile': 'Elevation',
        'dependencies': []
    })
    return 'IM_elevation added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    # local_ip = os.getenv('LOCAL_IP')
    # http://127.0.0.1:5000/microservice
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5004',
        'ip': im_ip
    })
    return 'IM_elevation deleted!', 200

@app.route('/', methods=["POST","GET"])
def get_elevation():
    input = request.data.decode('utf-8')
    input_json = json.loads(input)
    lat = str(input_json['latitude'])
    lon = str(input_json['longitude'])
    key = lat + ',' + lon
    
    elevation_url = 'https://api.opentopodata.org/v1/test-dataset?locations='
    r = requests.get(f'{elevation_url}{key}')
    js = r.json()
    if 'error' in js:
        json_response = jsonify(
            errorMessage = 'Invalid location input!'
        )
        now = datetime.now().timestamp()
        json_response.age = int(now)
        json_response.cache_control.max_age = int(now) + 1800
        return json_response
    json_response = jsonify(
        elevation = js['results'][0]['elevation']
    )
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 1800
    return json_response