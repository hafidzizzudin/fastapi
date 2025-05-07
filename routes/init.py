from fastapi import FastAPI

from routes.abstract import AbstractRouter


class Router:
    def __init__(self, app: FastAPI, routers: list[AbstractRouter]):
        self.app = app
        self.routers = routers

    def init(self):
        for router in self.routers:
            router.init()
