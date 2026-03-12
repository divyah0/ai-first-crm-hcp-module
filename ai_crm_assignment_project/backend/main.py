
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="AI First CRM - HCP Module")

class Interaction(BaseModel):
    doctor_name: str
    hospital: Optional[str] = None
    interaction_type: Optional[str] = None
    discussion_notes: str
    meeting_date: str
    follow_up_date: Optional[str] = None

fake_db = []

@app.get("/")
def root():
    return {"message": "AI CRM Backend Running"}

@app.post("/log_interaction")
def log_interaction(data: Interaction):
    record = data.dict()
    fake_db.append(record)
    return {"message": "Interaction logged successfully", "data": record}

@app.get("/interactions")
def get_interactions():
    return {"records": fake_db}
