from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/verify_ticket', methods=['POST'])
def verify_ticket():
    if 'file' not in request.files:
        return jsonify({'valid': False, 'message': 'No file uploaded'})

    file = request.files['file']

    # Save the file temporarily (optional, for future processing)
    file_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(file_path)

    # Placeholder logic for now (since no real image reading/QR scanner is done)
    # You can replace this with actual image/QR code reading logic
    filename = file.filename.lower()
    if 'cas' in filename or 'zaeden' in filename or 'atif' in filename:
        return jsonify({'valid': True, 'message': 'Valid Ticket'})
    else:
        return jsonify({'valid': False, 'message': 'Invalid Ticket'})

if __name__ == '__main__':
    app.run(debug=True)
