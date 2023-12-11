import requests
from fastapi import APIRouter, status, HTTPException

from settings.constants import URL_NOW, URL_FORECAST, HEADERS_NOW, HEADERS_FORECAST

params = {"q": f"akdjdfjdfjnm"}
response = requests.get(URL_NOW, headers=HEADERS_NOW, params=params)
print(response.json())
# if response.status_code == 400:
#     raise HTTPException(status_code=400, detail="Item not found")
#     print(response)
# elif response.status_code == 404:
#     raise HTTPException(status_code=404, detail="Bad gateway")
# else:
#     response.raise_for_status()