from datetime import timedelta, date
from fastapi import APIRouter, status, HTTPException
import requests

from app.schemas.request import Request
from app.schemas.weather_data import WeatherData
from app.settings.constants import URL_NOW, URL_FORECAST, HEADERS_NOW, HEADERS_FORECAST


router = APIRouter(prefix="/weather", tags=["Weather"])

@router.post("/get_now")
def get_current_wether(request: Request) -> WeatherData:
    """
    Create an item with all the information:

    - **country**: you can put the name of country in ru/en
    - **city**: required city name
    - **when**: you did't have to put the date (default=now)
    """
    params = {"q": f"{request.city}"}

    response = requests.get(URL_NOW, headers=HEADERS_NOW, params=params)
    if response.status_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"City not found")
    elif response.status_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Server is not aviable now")
    else:
        try:
            response = response.json()["current"]
            temp_celsium = str(response["temp_c"])
            is_precipitation = (response["precip_mm"] > 0)
            return WeatherData(temp_celsium=temp_celsium, is_precipitation=is_precipitation)
        except Exception as e:
            raise e
    

@router.post("/get_forecast")
def get_forecast(request: Request) -> WeatherData:
    """
    Create an item with all the information:

    - **country**: you can put the name of country in ru/en
    - **city**: required city name
    - **when**: it must be between today and next 14 days in yyyy-MM-dd format 
    """
    if request.when > (date.today() +  timedelta(days=14)):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Date must be between today and next 14 day")
    params = {"q":f"{request.city}", "dt": f"{request.when}"}

    response = requests.get(URL_FORECAST, headers=HEADERS_FORECAST, params=params)
    if response.status_code == 400:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"City not found")
    elif response.status_code == 404:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Server is not aviable now")
    else:
        try:
            response = response.json()["forecast"]["forecastday"][0]["day"]
            temp_celsium = str(response["avgtemp_c"])
            is_precipitation = (response["daily_will_it_snow"] or response["daily_will_it_rain"])
            return WeatherData(temp_celsium=temp_celsium, is_precipitation=is_precipitation)
        except Exception as e:
            raise e
