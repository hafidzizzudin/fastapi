from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# curl http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}


# curl http://127.0.0.1:8000/items/123?q=sdsd
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


class Item(BaseModel):
    name: str
    description: Union[str, None] = None  # add = None to make it optional
    price: float = None
    tax: Union[float, None] = None


@app.post("/item/")
async def create_item(item: Item):
    return item


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item": item}
