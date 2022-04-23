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
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json=
    {
        'port': '5005',
        'ip': im_ip,
        'name': 'State population',
        'creator': 'Boda Song',
        'tile': 'State population',
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
    return 'IM_state_population added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5005',
        'ip': im_ip
    })
    return 'IM_state_population deleted!', 200


@app.route('/', methods=["POST","GET"])
def get_pop():
    input = request.data.decode('utf-8')
    input_json = json.loads(input)
    #print(input_json)

    if 'state' not in input_json:
        json_response = jsonify(
        errorMessage = 'Cannot find state!'
        )    
        now = datetime.now().timestamp()
        json_response.age = int(now)
        json_response.cache_control.max_age = int(now) + 1800
        print(json_response.headers)
        return json_response

    state = input_json['state']

    # A dictionary transforming state abbrevations to full state names
    all_states = {
        'AL': 'Alabama',
        'AK': 'Alaska', 
        'AZ': 'Arizona', 
        'AR': 'Arkansas', 
        'CA': 'California',
        'CO': 'Colorado', 
        'CT': 'Connecticut',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'HI': 'Hawaii',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'IA': 'Iowa',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'ME': 'Maine',
        'MD': 'Maryland',
        'MA': 'Massachusetts',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MS': 'Mississippi',
        'MO': 'Missouri',
        'MT': 'Montana',
        'NE': 'Nebraska',
        'NV': 'Nevada',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NY': 'New York',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VT': 'Vermont',
        'VA': 'Virginia',
        'WA': 'Washington',
        'WV': 'West Virginia',
        'WI': 'Wisconsin',
        'WY': 'Wyoming'
    }
    state_fullname = all_states[state]
    
    pop_url = 'https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest'
    r_pop = requests.get(f'{pop_url}')
    pop_js = r_pop.json()
    data_block = pop_js['data']
    for data in data_block:
        if data['State'] == state_fullname:
            json_response = jsonify(
                state_population = data['Population']
            )
            now = datetime.now().timestamp()
            json_response.age = int(now)
            json_response.cache_control.max_age = int(now) + 1800
            print(json_response.headers)
            return json_response

    json_response = jsonify(
        errorMessage = 'Cannot find state!'
    )    
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 1800
    print(json_response.headers)
    return json_response
