# Project MIX: Information Microservices Documentation

**City IM** (Owned by Boda Song)

Find the name of the city at a given geographical location.

Input: a geographical location, in the form of {latitude, longitude}

Output: a JSON object, containing the city name, the accurate latitude and longitude of the city.

Example input: {40.1125, -88.2284}

Example output:

```json
{
  "city": "Urbana",
  "lat": 40.110126,
  "lon": -88.197323
}
```



**State IM** (Owned by Boda Song)

Find the state which the geographical location is in.

Input: a geographical location, in the form of {latitude, longitude}

Output: a JSON object, containing the state.

Example input: {40,1125,-88.2284}

Example output:

```json
{
  "state": "IL"
}
```



**Weather IM** (Owned by Harry Xia)

Find the current weather of the location, including the temperature, wind speed, wind direction, short forecast and detailed forecast.

Input: a geographical location, in the form of {latitude, longitude}

Output: a JSON object, containing the temperature, wind speed, wind direction, short forecast and detailed forecast.

Example input: {40.1125,-88.2284}

Example output: 

```json
{
   "detailedForecast": "Scattered rain and snow showers before 3am. Mostly cloudy, with a low around 32. West wind around 15 mph, with gusts as high as 25 mph. Chance of precipitation is 20%.",
    "shortForecast": "Scattered Rain And Snow Showers",
    "temperature": 32,
    "windDirection": "W",
    "windSpeed": "15 mph"
}
```



**Elevation IM** (Owned by Boda Song)

Return the elevation of the input location, in meters.

Input: a geographical location, in the form of {latitude, longitude}

output: a JSON object, containing the elevation value.

Example input: {40,-80} 

Exmaple output:

```json
{
  "elevation": 281
}
```



**State Population IM**(Owned by Boda Song)

This IM is based on the result from State IM.

Return the total population of the state where the location is in, data collected on 2019.

Input: The state abbreviation which the location is in, such as 'PA', from the State IM

Output: The state population

Example input: ''PA"

Example output:

```json
{
  "state_population": 12801989
}
```



**Timezone IM**(Owned by Harry Xia)

Return the timezone that the input location is in.

Input: a geographical location, in the form of {latitude, longitude}

Output: The timezone which the location is in

Example input: {40,-80}

Example output:

```json
{
  "timeZone": "America/New_York"
}
```



**State daily positive COVID cases IM**(Owned by Harry Via)

This IM is based on the result of the State IM

Returns the daily COVID positive cases of the state which the location is in.

Input: a geographical location, in the form of {latitude, longitude}

Output: The daily COVID positive cases

Example input: {40,-80}

Example output:

```json
{
  "state_positive_increase": 1658
}
```



**Error Handling**

​	All the errors are reflected by the final response on the frontend.

 1. If the input location is not in the form {latitude,longitude}, or contains irrelevant character, or is not a valid geographical location in the US, the response will be

    ```json
    {
      "errorMessage": "Invalid geographical location!"
    }
    ```



2. If the input location is valid, but the weather forecast is not available at that location, the city IM and state IM can still return the information, but the weather IM will return an error message.

   ```json
   # The input is {20,-155}, Hawaii Islands. National weather forecast is not available at that location.
   {
     "city": "Honomu",
     "lat": 19.8701,
     "lon": -155.10993,
     "state": "HI",
     "weather": "Weather forecast unavailable at this location!"
   }
   ```

   

3. All the other errors will have a same response like (1).

