from fastapi import FastAPI, UploadFile, Form, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import sqlite3
from PIL import Image
from pyzbar.pyzbar import decode
import os

app = FastAPI()

# -------------------- CORS Middleware --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- DB Check Function --------------------
def check_ticket_in_db(ticket_id: str):
    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute('SELECT status FROM tickets WHERE lower(ticket_id) = ?', (ticket_id.lower(),))
    result = cursor.fetchone()
    conn.close()
    return result

# -------------------- QR Code/Barcode Reader --------------------
def scan_ticket_from_image(image_path: str):
    try:
        image = Image.open(image_path)
        decoded_objects = decode(image)
        for obj in decoded_objects:
            return obj.data.decode('utf-8')  # Return first decoded QR/barcode data as string
        return None  # No QR/barcode found
    except Exception as e:
        print("Error reading QR:", e)
        return None

# -------------------- API Endpoint --------------------
@app.post("/validate_ticket")
async def validate_ticket(
    ticket_id: str = Form(None),  # Form input optional
    file: UploadFile = File(None)  # File upload optional
):
    if not ticket_id and not file:
        raise HTTPException(status_code=400, detail="Please provide a Ticket ID or upload a file.")

    # ---------------- Direct Ticket ID Input ----------------
    if ticket_id:
        result = check_ticket_in_db(ticket_id.strip())
        if result and result[0] == 'valid':
            return JSONResponse(content={"message": "Valid Ticket ✅"})
        else:
            return JSONResponse(content={"message": "Invalid Ticket ❌"})

    # ---------------- File Upload & QR/Barcode Scan ----------------
    if file:
        os.makedirs('uploads', exist_ok=True)
        file_path = os.path.join('uploads', file.filename)
        await file.seek(0)
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())

        # Scan for ticket ID from QR/barcode inside the image
        extracted_ticket_id = scan_ticket_from_image(file_path)

        if extracted_ticket_id:
            result = check_ticket_in_db(extracted_ticket_id.strip())
            if result and result[0] == 'valid':
                return JSONResponse(content={"message": f"Valid Ticket ✅ ({extracted_ticket_id})"})
            else:
                return JSONResponse(content={"message": "Invalid Ticket ❌"})
        else:
            return JSONResponse(content={"message": "No valid QR/Barcode found in image ❌"})
