from datetime import date
from pydantic import BaseModel

class Request(BaseModel):
    country: str | None = "Russia"
    city: str = "Saint Peterburg"
    when: date | None = date.today()
