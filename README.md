# Weather Forecast with API ⛅

### A simple web-service which can view real-time weather data and forecasts for other locations worldwide.
- Used FastAPI to create the API.
- Accessed Data using RapidAPI and WheaterAPI
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
Also you have to create file .env with your API keys. By default
'''
API_KEY_NOW=None
API_HOST_NOW=None
API_KEY_FORECAST=None
'''
