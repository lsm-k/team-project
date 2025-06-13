import sqlite3
import os
from dataclasses import dataclass

from cold_storage import db as cs_db

con = sqlite3.connect(cs_db.db_path)
con.row_factory = sqlite3.Row
cursor = con.cursor()


@dataclass
class Setting:
    name: str = ""
    value: str = ""


class Database:
    def reset(self):
        cursor.execute("DROP TABLE IF EXISTS Setting")
        con.commit()
        self.setting_table()

    @classmethod
    def setting_table(cls):
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS Setting (
            name TEXT NOT NULL,
            value TEXT NOT NULL
        )
        """
        )
        con.commit()

    @classmethod
    def create(cls, name: str, value: str):
        sql = """
        INSERT INTO Setting (name, value) VALUES (?, ?)
        """
        cursor.execute(sql, (name, value))
        con.commit()
        return cursor.lastrowid

    @classmethod
    def get_with_name(cls, name: str):
        sql = """
        SELECT * FROM Setting WHERE name = ?
        """
        cursor.execute(sql, (name,))
        row = cursor.fetchone()
        if row:
            return Setting(**row)
        return None

    @classmethod
    def update(cls, setting: Setting):
        sql = """
        UPDATE Setting SET value = ? WHERE name = ?
        """
        cursor.execute(sql, (setting.value, setting.name))
        con.commit()
        return cursor.rowcount > 0

    @classmethod
    def get_gemini_api_key(cls):
        setting = cls.get_with_name("gemini_api_key")
        if setting is not None:
            return setting
        return None

    @classmethod
    def get_font_size(cls):
        setting = cls.get_with_name("font_size")
        if setting is not None:
            return setting
        return None
