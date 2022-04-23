import os
import requests
from datetime import datetime
import json
# export FLASK_APP=IM_state

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET','PUT'])
def add():
    # local_ip = os.getenv('LOCAL_IP')
    im_ip = os.getenv('IM_IP')

    # http://127.0.0.1:5000/microservice
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5007',
        'ip': 'http://172.22.150.47',
        'name': 'Daily COVID Increase',
        'creator': 'Harry Xia',
        'tile': 'Daily COVID Increase',
        'dependencies': [
            {
            'port': '5001',
            'ip': 'http://172.22.150.47',
            'name': 'State',
            'creator': 'Boda Song',
            'tile': 'State',
            'dependencies': []
            }
        ]
    })
    return 'IM_COVID added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    # local_ip = os.getenv('LOCAL_IP')
    im_ip = os.getenv('IM_IP')

    # http://127.0.0.1:5000/microservice
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5007',
        'ip': 'http://172.22.150.47'
    })
    return 'IM_COVID deleted!', 200

@app.route('/', methods=["POST","GET"])
def get_pop():
    input = request.data.decode('utf-8')
    input_json = json.loads(input)
    print(input_json)

    if 'state' not in input_json:
        json_response = jsonify (errorMessage = 'Invalid location for COVID IM!')
        now = datetime.now().timestamp()
        json_response.age = int(now)
        json_response.cache_control.max_age = int(now) + 3600
        return json_response

    state = input_json['state']
    state_abrev = state.lower()

    
    covid_url = 'https://api.covidtracking.com/v1/states/'
    tail = "current.json"
    c = requests.get(f'{covid_url}/{state_abrev}/{tail}')
    covid_js = c.json()
    posIncrese = covid_js["positiveIncrease"]
 
    json_response = jsonify (state_positive_increase = posIncrese)
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 3600
    return json_response
        