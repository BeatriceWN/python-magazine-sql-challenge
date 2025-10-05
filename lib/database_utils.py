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
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS author(
        id INTEGER PRIMARY KEY AUTOINCREMENT
        name TEXT NOT NULL
    )               
                   
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS magazines(
        id INTEGER PRIMARY AUTOINCREMENT
        name TEXT NOT NULL
        category TEXT NOT NULL
    )               
    """)
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS articles(
        id INTEGER PRIMARY AUTOINCREMENT
        title TEXT NOT NULL
        author_id INTEGER NOT NULL
        magazine_id NOT NULL
        FOREIGN KEY(author_id) REFERENCES authors(id) 
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    )         
    """)
    conn.commit()
    conn.close()
    