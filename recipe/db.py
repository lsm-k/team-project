import sqlite3
import os
from dataclasses import dataclass

db_path = os.path.join(os.path.dirname(__file__), "recipe.db")
con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
cursor = con.cursor()


@dataclass
class Recipe:
    id: int = 0
    url: str = ""
    thumbnail_url: str = ""
    title: str = ""
    description: str = ""
    servings: str = ""
    cooking_time: str = ""
    level: str = ""
    ingredients: str = ""
    steps: str = ""


class Database:
    @classmethod
    def setting_table():
        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS RecipeInfo (
            id	INTEGER NOT NULL,
            url	TEXT NOT NULL,
            thumbnail_url TEXT NOT NULL,
            title TEXT NOT NULL,
            description	TEXT NOT NULL,
            servings TEXT,
            cooking_time TEXT,
            level TEXT,
            ingredients	TEXT NOT NULL,
            steps TEXT NOT NULL
        )
        """
        )
        connection.commit()

    @classmethod
    def get():
        sql = """
        SELECT * FROM RecipeInfo
        """
        cursor.execute(sql)
        return [Recipe(**row) for row in cursor.fetchall()]

    # get with limit
    @classmethod
    def get_with_limit(cls, limit: int):
        sql = """
        SELECT * FROM RecipeInfo LIMIT ?
        """
        cursor.execute(sql, (limit,))
        return [Recipe(**row) for row in cursor.fetchall()]
