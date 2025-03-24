import random

def detect_ticket_fraud(image_path):
    """
    Simulate AI fraud detection for ticket images.
    """
    print(f"Processing image: {image_path}")

    # Randomly return if the ticket is real or tampered
    result = random.choice(["Valid Ticket", "Tampered Ticket", "Fake Ticket"])
    return result
