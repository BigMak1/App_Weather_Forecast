from pydantic import BaseModel

class WeatherData(BaseModel):
    temp_celsium: str = None
    is_precipitation: bool = None
