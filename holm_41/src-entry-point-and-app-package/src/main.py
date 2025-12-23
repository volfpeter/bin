from fastapi import FastAPI

from my_app.main import init_holm

app = FastAPI()
init_holm(app)
