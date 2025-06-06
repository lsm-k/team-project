import sqlite3
import os
from dataclasses import dataclass

db_path = os.path.join(os.path.dirname(__file__), "db.sqlite3")
connection = sqlite3.connect(db_path)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()


@dataclass
class Ref:
    id: int = 0
    Food_name: str = ""
    Amount: int = 0
    Expiration_date: str = ""
    Food_type: str = ""
    is_favorite: bool = False
    created_at: str = ""


class Database:
    def setting_table(self):
        # 테이블 생성
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Ref (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                Food_name TEXT NOT NULL,
                Amount INTEGER NOT NULL,
                Expiration_date TEXT NOT NULL,
                Food_type TEXT NOT NULL,
                is_favorite INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
        """
        )
        connection.commit()

    @classmethod
    def data_insert(cls, Food_name, Amount, Expiration_date, Food_type):
        # 데이터 삽입
        cursor.execute(
            """
            INSERT INTO Ref(Food_name, Amount, Expiration_date, Food_type)
            VALUES(?, ?, ?, ?)
        """,
            (Food_name, Amount, Expiration_date, Food_type),
        )
        connection.commit()
        return cursor.lastrowid

    @classmethod
    def delete(cls, ref_id: int):
        # 데이터 삭제
        cursor.execute(
            """
            DELETE FROM Ref WHERE id = ?
            """,
            (ref_id,),
        )

        connection.commit()

        return cursor.rowcount > 0

    def data_edit_name(self, Food_name, New_Food_name):
        # 식품 이름 데이터 수정
        cursor.execute(
            """
            UPDATE Ref SET Food_name = ? WHERE Food_name = ?
        """,
            (New_Food_name, Food_name),
        )
        connection.commit()

    def data_edit_amount(self, Food_name, Amount):
        # 수량 데이터 수정
        cursor.execute(
            """
            UPDATE Ref SET Amount = ? WHERE Food_name = ?
        """,
            (Amount, Food_name),
        )
        connection.commit()

    def data_edit_expiration(self, Food_name, Expiration_date):
        # 유통기한 데이터 수정
        cursor.execute(
            """
            UPDATE Ref SET Expiration_date = ? WHERE Food_name = ?
        """,
            (Expiration_date, Food_name),
        )
        connection.commit()

    def data_edit_type(self, Food_name, Food_type):
        # 카테고리 데이터 수정
        cursor.execute(
            """
            UPDATE Ref SET Food_type = ? WHERE Food_name = ?
        """,
            (Food_type, Food_name),
        )
        connection.commit()

    @classmethod
    def get_all(cls):
        # 모든 데이터 조회
        sql = """
        SELECT * FROM Ref
        """
        cursor.execute(sql)
        return [Ref(**row) for row in cursor.fetchall()]
    
    @classmethod
    def get_food_name(cls):
        # 식품 이름 전부 조회
        sql = """
        SELECT Food_name FROM Ref
        """

        cursor.execute(sql)
        return [row[0] for row in cursor.fetchall()]
    
    @classmethod
    def get_food_name(cls):
        # 식품 이름 전부 조회
        sql = """
        SELECT Food_name FROM Ref
        """

        cursor.execute(sql)
        return [row[0] for row in cursor.fetchall()]

    @classmethod
    def update_favorite(cls, ref_id: int, is_favorite: bool):
        sql = """
        UPDATE Ref SET is_favorite = ? WHERE id = ?
        """
        cursor.execute(sql, (1 if is_favorite else 0, ref_id))
        connection.commit()
        return cursor.rowcount > 0
