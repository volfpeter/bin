from fastapi import FastAPI

from .subpackage.web.main import app as web_app

app = FastAPI()

app.mount("/", web_app)


@app.get("/status")
def status() -> str:
    return "OK"
