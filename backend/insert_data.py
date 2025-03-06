import sqlite3

# Connect to the database
conn = sqlite3.connect('tickets.db')
cursor = conn.cursor()

# Sample tickets
tickets = [
    # ✅ Legit tickets
    ("TIX1001", "Zayn Malik Live", "Zayn Malik", "2025-08-20", "JLN Stadium, Delhi", "Riya Sharma", "BookMyShow", True),
    ("TIX1002", "Arijit Singh Live", "Arijit Singh", "2025-09-15", "BKC Ground, Mumbai", "Aman Verma", "Paytm Insider", True),
    ("TIX1003", "Diljit Dosanjh Night", "Diljit Dosanjh", "2025-10-10", "Hyderabad Arena", "Sneha Kapoor", "Official Website", True),

    # ❌ Fake tickets (either tampered or bought from random sources)
    ("TIX9991", "Zayn Malik Live", "Zayn Malik", "2025-08-20", "JLN Stadium, Delhi", "Fake Buyer", "RandomWebsite123", False),
    ("TIX9992", "Arijit Singh Live", "Arijit Singh", "2025-09-15", "BKC Ground, Mumbai", "Scam Buyer", "FakeTickets.io", False),
]

# Insert the tickets
cursor.executemany('''
INSERT INTO tickets (ticket_id, event_name, artist_name, event_date, venue, buyer_name, purchase_platform, verified)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', tickets)

conn.commit()
conn.close()

print("Sample tickets inserted successfully.")
