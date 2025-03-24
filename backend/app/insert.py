import sqlite3

def is_ticket_valid(ticket_id):
    connection = sqlite3.connect('tickets.db')
    cursor = connection.cursor()
    
    cursor.execute('SELECT * FROM valid_tickets WHERE ticket_id = ?', (ticket_id,))
    result = cursor.fetchone()
    
    
    connection.close()
    
    if result:
        return True
    else:
        return False
