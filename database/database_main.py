import sqlite3 as sql
import os

db_path = os.path.join(os.path.dirname(__file__), "team_project_db.db")
connection = sql.connect(db_path)
curser = connection.cursor()

class Database:
    def default():
        #테이블 생성
        curser.execute("""
            CREATE TABLE IF NOT EXISTS Ref (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Food_name TEXT NOT NULL,
                Amount INTEGER NOT NULL,
                Expiration_date TEXT NOT NULL,
                Food_type TEXT NOT NULL
            )
        """)
    def data_insert(Food_name, Amount, Expiration_date, Food_type):
        # 데이터 삽입
        curser.execute(f"""
            INSERT INTO Ref(Food_name, Amount, Expiration_date, Food_type)
            VALUES('{Food_name}', {Amount} , '{Expiration_date}', '{Food_type}'),
        """)
    def data_delete(Food_name):
        #데이터 삭제
        curser.execute(f"""
            DELETE FROM Ref WHERE Food_name = '{Food_name}'
        """)
    def data_edit_name(Food_name, New_Food_name):
        # 식품 이름 데이터 수정
        curser.execute(f"""
            UPDATE Ref SET Food_name = '{New_Food_name}' WHERE Food_name = '{Food_name}'
        """)
    def data_edit_amount(Food_name, Amount):
        # 수량 데이터 수정
        curser.execute(f"""
            UPDATE Ref SET Amount = {Amount} WHERE Food_name = '{Food_name}'
        """)
    def data_edit_expiration(Food_name, Expiration_date):
        # 유통기한한 데이터 수정
        curser.execute(f"""
            UPDATE Ref SET Expiration_date = '{Expiration_date}' WHERE Food_name = '{Food_name}'
        """)
    def data_edit_type(Food_name, Food_type):
        # 카테고리 데이터 수정
        curser.execute(f"""
            UPDATE Ref SET Food_type = '{Food_type}' WHERE Food_name = '{Food_name}'
        """)


connection.commit()
connection.close()