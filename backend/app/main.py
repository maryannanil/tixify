from fastapi import FastAPI, HTTPException
from pathlib import Path
import json

app = FastAPI()

# Load the tickets data
data_path = Path(__file__).parent / "tickets.json"
with data_path.open() as file:
    tickets_data = json.load(file)


@app.post("/verify_ticket")
def verify_ticket(ticket: dict):
    mismatches = []

    # Find ticket by ticket_id
    for original_ticket in tickets_data:
        if original_ticket["ticket_id"] == ticket["ticket_id"]:
            # Check each field for mismatches
            for field in ["event", "location", "date", "source"]:
                if ticket.get(field) != original_ticket.get(field):
                    mismatches.append(field)
            
            if mismatches:
                return {
                    "verified": False,
                    "mismatches": mismatches,
                    "message": "Ticket verification failed due to mismatched details."
                }
            else:
                return {
                    "verified": True,
                    "message": "Ticket successfully verified."
                }

    # If no ticket_id match found
    raise HTTPException(status_code=404, detail="Ticket ID not found in our records.")
