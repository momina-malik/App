# get_db_connection.py
def get_db_connection():
    conn = sqlite3.connect('database.db')
    return conn