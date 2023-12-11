# Weather Forecast with API ⛅

### A simple web-service which can view real-time weather data and forecasts for other locations worldwide.
- Used FastAPI to create the API.
- Accessed Data using *[RapidAPI] and *[WheaterAPI]
- Used Deta for deploying the API


## How To Use 🔧:

From your command line, first clone this repo:

```bash
# Clone this repository
$ git clone https://github.com/BigMak1/App_Weather_Forecast.git

# Create docker image
$ docker build -t my_app .

# Run docker container with your port (replace 7000 -> on your option)
$ docker run -d -p 7000:8000 my_app

# Open page on local host with your port
$ open http://localhost:7000/docs

```  
Also you have to create file .env with your API keys to the path ``app/settings/``. By default
```  
API_KEY_NOW=None
API_HOST_NOW=None
API_KEY_FORECAST=None
```
Fill it.

## Actions

- ``get_now`` - get the current weather anywhere
- ``get_forecast`` - get the weather forecast anywhere but no more than 14 days in advance

## Input

```jsonc
{
    "country": string,
    "city": string,
    "when": datetime
}
```

## Output 

```jsonc
{
    "temp_celsium": string,
    "is_precipitation": bool
}

    [RapidAPI]: <https://rapidapi.com/weatherapi/api/weatherapi-com>
    [WheaterAPI]: <https://www.weatherapi.com/pricing.aspx>
