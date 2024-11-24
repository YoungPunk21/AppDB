# db.py

import sqlite3


def create_db():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                       name TEXT NOT NULL, 
                       email TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

def add_user(name, email):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute('''INSERT INTO users (name, email) 
                      VALUES (?, ?)''', (name, email))
    
    conn.commit()
    conn.close()

def get_users():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    cursor.execute('''SELECT * FROM users''')
    users = cursor.fetchall()
    
    conn.close()
    return users
