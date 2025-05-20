import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), "test.db")
connection = sqlite3.connect(db_path)
curser = connection.cursor()

curser.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

# 테이블 목록 출력
curser.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = curser.fetchall()
print("생성된 테이블", tables)  

connection.commit()
connection.close()