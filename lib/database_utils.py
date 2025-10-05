import sqlite3

DB_FILE = "magazine.db"

def get_connection():
    """return SQLite connection with FK enabled"""
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.ROM #to access columns by name
    conn.execute("PRAGMA Foreign_Keys = ON;")
    return conn

def create_table():
    """create a table for authors, magazines and articles"""
    conn = get_connection()
    cursor = conn.cursor()
    