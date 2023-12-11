from fastapi import FastAPI
import uvicorn
from routers.get_weather import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(router)


@app.get("/", tags=["Welcome"])
def home():
    return {"Message": "Welcome To Weather API"}
    

# if __name__ == "__main__":
#     uvicorn.run(app, reload=True)
# from fastapi import APIRouter, FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None

# app = FastAPI()
# router = APIRouter()

# @router.put("/items/")
# def create_item(item: Item):
#     return item

# app.include_router(router)