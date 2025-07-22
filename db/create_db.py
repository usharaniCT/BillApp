import sqlite3
import os

if not os.path.exists('db'):
    os.makedirs('db')

conn = sqlite3.connect('db/bills.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bills (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT NOT NULL,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        total REAL NOT NULL
    )
''')

conn.commit()
conn.close()

print("Database and table created successfully in 'db/bills.db'.")

