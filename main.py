from fastapi import FastAPI

app = FastAPI()


@app.get("/status-ping")
def ping():
    return {"status": "ok"}
