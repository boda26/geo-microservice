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
        'port': '5008',
        'ip': im_ip,
        'name': 'Total COVID death in the state',
        'creator': 'Boda Song',
        'tile': 'Total COVID death in the state',
        'dependencies': [
            {
            'port': '5001',
            'ip': im_ip,
            'name': 'State',
            'creator': 'Boda Song',
            'tile': 'State',
            'dependencies': []
            }
        ]
    })
    return 'IM COVID_death added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5008',
        'ip': im_ip
    })
    return 'IM COVID_death deleted!', 200

@app.route('/', methods=["POST","GET"])
def get_pop():
    input = request.data.decode('utf-8')
    input_json = json.loads(input)

    if 'state' not in input_json:
        json_response = jsonify (errorMessage = 'Invalid input, cannot find state!')
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
    deathTotal = covid_js["death"]
 
    json_response = jsonify (state_total_death = deathTotal)
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 3600
    return json_response
        