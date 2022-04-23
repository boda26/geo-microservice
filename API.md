# Project MIX: API Documentation

**Overview**

<img src="https://github.com/cs240-illinois/cs240-fa21-MIX_BFF-hxia5-boda2/blob/master/project-MIX/image-20211112212905367.png" />

Our MIX web service is composed of three parts: frontend, middleware and backend. The frontend is using the provided index.html, which displays the information. The middleware works as an interface which connects the frontend and the backend, combining all the responses from the IMs into a single response and send to the frontend. The backend is consisted of different IMs, and each of the IM provides a single piece of information.

The middleware and each IM uses a different address in order to run separately.

Addresses:

Middleware	http://127.0.0.1:5000

City IM	http://127.0.0.1/5001

State IM http://127.0.0.1/5002

Weather IM http://127.0.0.1/5003

Elevation IM http://127.0.0.1/5004

State_population IM http://127.0.0.1/5005

Timezone IM http://127.0.0.1/5006

COVID_IM http://127.0.0.1/5007





**Requests and Responses**

Request between frontend and middleware

​	Forms: POST, GET

​	http://127.0.0.1/5000

Request between middleware and backend

​	Forms: POST, GET

​	http://127.0.0.1/5001/{lat},{lon}

​	http://127.0.0.1/5002/{lat},{lon}

​	http://127.0.0.1/5003/{lat},{lon}



Responses:

​	All the responses are JSON objects

​	Response between the middleware and the frontend	

```json
{
  "city": "Urbana",
  "lat": 40.110126,
  "lon": -88.197323,
  "state": "IL",
  "weather": {
    "detailedForecast": "Scattered rain and snow showers before 3am. Mostly cloudy, with a low around 32. West wind around 15 mph, with gusts as high as 25 mph. Chance of precipitation is 20%.",
    "shortForecast": "Scattered Rain And Snow Showers",
    "temperature": 32,
    "windDirection": "W",
    "windSpeed": "15 mph"
  }
}
```

​	Response between the city IM and the middleware

```json
{	
	"city": "Urbana",
  "lat": 40.110126,
  "lon": -88.197323
}
```

​	Response between the state IM and the middleware

```json
{
	"state": "IL"
}
```

​	Response between the weather IM and the middleware

```json
{
	"detailedForecast": "Scattered rain and snow showers before 3am. Mostly cloudy, with a low around 32. West wind around 15 mph, with gusts as high as 25 mph. Chance of precipitation is 20%.",
  "shortForecast": "Scattered Rain And Snow Showers",
  "temperature": 32,
  "windDirection": "W",
  "windSpeed": "15 mph"
}
```



**Adding and deleting IMs**

IMs are separated in single folder inside the MIX directory.

The folders are named by "IM_{name of the IM}" uniquely, and each IM has its own folder.

Each IM folder consists of two files, IM_{name of the IM}.py (the IM python file) and .env (the file for the environmental parameters). The .env file contains the port it is running on and the API information the IM uses.

IMs can work separately on its own address, and they are added to the middleware by adding their addresses inside the .env file in the project-MIX directory, and combining the response of the single IM into the final response from the middleware to the frontend.

IMs are deleted by removing the address from the .env file and excluding all their response from the middleware.





**Dependencies**

Commands to run the MIX service

 1. Commands to run the middleware

    ```python
    # Inside the project-MIX folder
    flask run
    ```



2. Commands to run each IM

   ```
   # Inside the folder of each IM
   export FLASK_APP = {name of the IM python file}
   flask run
   ```



External Resources

	1.	National Weather Service API: The national weather service API, returning the geographical location and weather forecast of the request time based on the location {latitude, longitude}. (https://www.weather.gov/documentation/services-web-api)
	2.	Open Topo Data: a REST API server for your elevation data. (https://www.opentopodata.org/)
	3.	Data USA API: The Data USA API allows users to explore the entire database using carefully constructed query strings, returning data as JSON results. (https://datausa.io/about/api/)
	4.	The COVID Tracking Project Data API: The The COVID Tracking Project Data API, provides data for every states related to COVID. (https://covidtracking.com/data/api)

​	
