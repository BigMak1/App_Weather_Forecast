import os
from dotenv import load_dotenv


load_dotenv()

URL_NOW = "https://weatherapi-com.p.rapidapi.com/current.json"
HEADERS_NOW = {
    "X-RapidAPI-Key": os.getenv("API_KEY_NOW"),
    "X-RapidAPI-Host": os.getenv("API_HOST_NOW"),
}

URL_FORECAST = "http://api.weatherapi.com/v1/forecast.json"
HEADERS_FORECAST = headers = {
	"Content-Type": "application/json",
    "key": os.getenv("API_KEY_FORECAST")
}
