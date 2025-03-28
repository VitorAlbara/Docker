import pymongo
from typing import Union
from fastapi import FastAPI
import os
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

MONGODB_URI = os.getenv("MONGODB_URI")

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}



@app.get("/aula")
def aula(item: Item):
    myclient = pymongo.MongoClient("mongodb://mongodb1:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(item)