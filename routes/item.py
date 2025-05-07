from typing import Union

from fastapi import FastAPI

from models.item import Item
from repository.item import ItemRepository
from routes.abstract import AbstractRouter


class ItemRouter(AbstractRouter):
    def __init__(self, app: FastAPI, repo: ItemRepository):
        self.app = app
        self.repo = repo

    def init(self):
        # curl http://127.0.0.1:8000/
        @self.app.get("/items")
        def read_items():
            return {"items": self.repo.get_items()}

        # curl http://127.0.0.1:8000/items/123?q=sdsd
        @self.app.get("/item/{item_id}")
        def read_item(item_id: int, q: Union[str, None] = None):
            return {"item": self.repo.get_item(item_id), "q": q}

        @self.app.post("/item/")
        async def create_item(item: Item):
            new_item = self.repo.create_item(item)
            return {"item": new_item}

        @self.app.put("/item/{item_id}")
        async def update_item(item_id: int, item: Item):
            updated_item = self.repo.update_item(item_id, item)
            return {"item": updated_item}
