import sqlite3
import os
from dataclasses import dataclass

from cold_storage import db as cs_db

con = sqlite3.connect(cs_db.db_path)
con.row_factory = sqlite3.Row
cursor = con.cursor()


@dataclass
class FavoriteRef:
    id: int = 0
    ref_id: int = 0
    created_at: str = ""


class Database:
    @classmethod
    def setting_table(cls):
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS FavoriteRef (
            id	INTEGER PRIMARY KEY AUTOINCREMENT,
            ref_id INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
        """
        )
        con.commit()

    @classmethod
    def create(cls, ref_id: int):
        sql = """
        INSERT INTO FavoriteRef (ref_id, created_at)
        VALUES (?, datetime('now'))
        """
        cursor.execute(sql, (ref_id,))
        con.commit()
        return cursor.lastrowid

    @classmethod
    def get_with_ref_id(cls, ref_id: int):
        sql = """
        SELECT * FROM FavoriteRef WHERE ref_id = ?
        """
        cursor.execute(sql, (ref_id,))
        row = cursor.fetchone()
        if row:
            return FavoriteRecipe(**row)
        return None

    @classmethod
    def get_all(cls):
        sql = """
        SELECT * FROM FavoriteRef
        """
        cursor.execute(sql)
        return [FavoriteRef(**row) for row in cursor.fetchall()]

    @classmethod
    def delete(cls, ref_id: int):
        sql = """
        DELETE FROM FavoriteRef WHERE ref_id = ?
        """
        cursor.execute(sql, (ref_id,))
        con.commit()
        return cursor.rowcount > 0
