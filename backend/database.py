import sqlite3

# Connect to database (creates one if it doesn't exist)
conn = sqlite3.connect('tickets.db')
cursor = conn.cursor()

# Create the tickets table
cursor.execute('''
CREATE TABLE IF NOT EXISTS tickets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id TEXT UNIQUE,
    event_name TEXT,
    artist_name TEXT,
    event_date TEXT,
    venue TEXT,
    buyer_name TEXT,
    purchase_platform TEXT,
    verified BOOLEAN
)
''')

conn.commit()
conn.close()

print("Database and table created successfully.")
