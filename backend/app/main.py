from fastapi import FastAPI
import json
import os

app = FastAPI()

# Dynamically get the path of tickets.json
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(BASE_DIR, 'tickets.json')

# Load the JSON data
with open(json_path, 'r') as file:
    tickets_data = json.load(file)

@app.get("/")
def read_root():
    return {"message": "Welcome to Tixify!"}

@app.get("/tickets")
def get_tickets():
    return tickets_data
