from fastapi import FastAPI
from sqlalchemy import Engine
from sqlmodel import create_engine

from infra import settings
from repository.item import ItemRepository
from routes.init import Router
from routes.item import ItemRouter


def init_router(app: FastAPI) -> Router:
    repo = ItemRepository()
    item_router = ItemRouter(app, repo)

    return Router(app, [item_router])


def init_db() -> Engine:
    sqlite_url = f"sqlite:///{settings.settings.db_path}"
    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, connect_args=connect_args)
    return engine


db_engine = init_db()
app = FastAPI()
router = init_router(app)
router.init()
