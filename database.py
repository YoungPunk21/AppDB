import sqlite3

def connect_to_db(db_name="app.db"):
    conn = sqlite3.connect(db_name)
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()

def insert_user(conn, name, age):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (name, age)
        VALUES (?, ?)
    ''', (name, age))
    conn.commit()

def fetch_all_users(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()
