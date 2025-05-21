from fastapi import FastAPI, HTTPException
from models import Receipt
from uuid import uuid4
import storage_db
from logic import calculate_points

app = FastAPI()


@app.get("/status-ping")
def ping():
    return {"status": "ok"}


@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid4())
    points = calculate_points(receipt)
    storage_db.db[receipt_id] = {"points": points}
    return {"id": receipt_id}


@app.get("/receipts/{id}/points")
def get_points(id: str):
    if id not in storage_db.db:
        raise HTTPException(
            status_code=404, detail="No receipt found for that ID.")
    return {"points": storage_db.db[id]["points"]}
