from fastapi import FastAPI

from repository.item import ItemRepository
from routes.init import Router
from routes.item import ItemRouter


def init_router(app: FastAPI) -> Router:
    repo = ItemRepository()
    item_router = ItemRouter(app, repo)

    return Router(app, [item_router])


app = FastAPI()
router = init_router(app)
router.init()
