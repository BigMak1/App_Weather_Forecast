from fastapi import FastAPI

from app.routers.get_weather import router

app = FastAPI()

app.include_router(router)


@app.get("/", tags=["Welcome"])
def home():
    return {"Message": "This is the weather forecast"}
    