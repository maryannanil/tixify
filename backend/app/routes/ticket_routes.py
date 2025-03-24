import os
import sqlite3
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from ai_model import detect_ticket_fraud  # AI model for image verification

ticket_bp = Blueprint('ticket_bp', __name__)

UPLOAD_FOLDER = "app/static/uploads"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# ✅ Check ticket by ID
@ticket_bp.route('/verify', methods=['GET'])
def verify_ticket():
    ticket_id = request.args.get('ticket_id')

    if not ticket_id:
        return jsonify({"error": "Ticket ID is required"}), 400

    conn = sqlite3.connect('tickets.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE ticket_id = ?", (ticket_id,))
    ticket = cursor.fetchone()
    conn.close()

    if ticket:
        return jsonify({"ticket_id": ticket_id, "status": "Valid", "event": ticket[2]})
    else:
        return jsonify({"ticket_id": ticket_id, "status": "Invalid"}), 404

# ✅ Upload ticket image for AI fraud detection
@ticket_bp.route('/upload', methods=['POST'])
def upload_ticket():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # 🔍 Run AI fraud detection
        fraud_result = detect_ticket_fraud(filepath)

        return jsonify({"filename": filename, "fraud_check": fraud_result})
    
    return jsonify({"error": "Invalid file format"}), 400
