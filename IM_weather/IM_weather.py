#
import os
import requests
from datetime import datetime
import json
# export FLASK_APP=IM_weather

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
im_ip = 'http://172.22.150.47'

@app.route('/add', methods=['GET','PUT'])
def add():
    # local_ip = os.getenv('LOCAL_IP')
    # http://127.0.0.1:5000/microservice
    requests.put('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5003',
        'ip': im_ip,
        'name': 'Weather',
        'creator': 'Harry Xia',
        'tile': 'Weather',
        'dependencies': []
    })
    return 'IM_weather added!',200


@app.route('/delete', methods=['GET','DELETE'])
def delete():
    # local_ip = os.getenv('LOCAL_IP')
    # http://127.0.0.1:5000/microservice
    requests.delete('http://cs240-adm-01.cs.illinois.edu:5000/microservice', json={
        'port': '5003',
        'ip': im_ip
    })
    return 'IM_weather deleted!', 200


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

    forecast_url = js["properties"]["forecast"]
    f = requests.get(f'{forecast_url}')
    js1 = f.json()
    if ('correlationId') in js1:
        json_response = jsonify(
            errorMessage = 'Invalid geographical location!',
        )
        now = datetime.now().timestamp()
        json_response.age = int(now)
        json_response.cache_control.max_age = int(now) + 1800
        return json_response

    temp = js1["properties"]["periods"][0]["temperature"]
    wind_speed = js1["properties"]["periods"][0]["windSpeed"]
    wind_dir = js1["properties"]["periods"][0]["windDirection"]
    short_forecast = js1["properties"]["periods"][0]["shortForecast"]
    detailed_forecast = js1["properties"]["periods"][0]["detailedForecast"]

    json_response = jsonify(
        temperature = temp,
        windSpeed = wind_speed,
        windDirection = wind_dir,
        shortForecast = short_forecast,
        detailedForecast = detailed_forecast
    ) 
    now = datetime.now().timestamp()
    json_response.age = int(now)
    json_response.cache_control.max_age = int(now) + 1800
    return json_response