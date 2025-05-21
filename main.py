from fastapi import FastAPI
from models import Receipt
from uuid import uuid4
import storage_db

app = FastAPI()


@app.get("/status-ping")
def ping():
    return {"status": "ok"}


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid4())
    storage_db.db[receipt_id] = {"points": 1111}  # Test Value
    return {"id": receipt_id}
