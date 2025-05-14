import sqlite3 as sql
import os

db_path = os.path.join(os.path.dirname(__file__), "team_project_db.db")
connection = sql.connect(db_path)
curser = connection.cursor()

#테이블 생성
curser.execute("""
    CREATE TABLE IF NOT EXISTS Ref (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        Food_name TEXT NOT NULL,
        Amount INTEGER NOT NULL,
        Expiration_date TEXT NOT NULL
    )
""")

# 데이터 삽입
# curser.execute("""
#     INSERT INTO Ref(Food_name, Amount, Expiration_date)
#     VALUES('바나나', 2 , '2025-12-12')
# """)

#데이터 제거
# curser.execute("""
#                DELETE FROM Ref WHERE Food_name = '바나나'
# """)

# 데이터 수정
# curser.execute("""
#                UPDATE Ref SET Amount = 3 WHERE Food_name = '바나나'
# """)



connection.commit()
connection.close()