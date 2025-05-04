from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: Union[str, None] = None  # add = None to make it optional
    price: float = None
    tax: Union[float, None] = None


items = {
    1: Item(id=1, name="Foo", description="A very nice Item", price=10.00, tax=1.00),
    2: Item(id=2, name="Bar", description="A very nice Item", price=10.00, tax=1.00),
}


# curl http://127.0.0.1:8000/
@app.get("/items")
def read_items():
    item_list = [item for item in items.values()]
    return {"items": item_list}


# curl http://127.0.0.1:8000/items/123?q=sdsd
@app.get("/item/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    item = items.get(item_id)
    return {"item": item, "q": q}


@app.post("/item/")
async def create_item(item: Item):
    last_id = max(items.keys())
    item.id = last_id + 1
    items[item.id] = item
    return {"item": item}


@app.put("/item/{item_id}")
async def update_item(item_id: int, item: Item):
    items[item_id] = item
    return {"item": item}
