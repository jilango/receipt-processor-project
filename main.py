from fastapi import FastAPI
from models import Receipt
from uuid import uuid4

app = FastAPI()


@app.get("/status-ping")
def ping():
    return {"status": "ok"}


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    return {"id": str(uuid4())}
