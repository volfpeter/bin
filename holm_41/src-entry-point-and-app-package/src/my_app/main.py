from fastapi import FastAPI
from holm import App


def init_holm(app: FastAPI) -> None:
    App(app=app)
