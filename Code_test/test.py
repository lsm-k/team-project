import sqlite3

connection = sqlite3.connect("test.db")
curser = connection.cursor()

curser.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL,
""")

connection.commit()
connection.close()