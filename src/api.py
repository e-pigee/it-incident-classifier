from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "TicketIQ API is running"}

class TicketRequest(BaseModel):
    description: str

@app.post("/predict")
async def predict_ticket(ticket: TicketRequest):
    return {"description": ticket.description} 