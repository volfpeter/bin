import uvicorn
from holm import App

app = App()

def run_app():
    uvicorn.run("my_app.main:app", port=5000, log_level="info")
