import sqlite3
import os
from dataclasses import dataclass

db_path = os.path.join(os.path.dirname(__file__), "recipe.db")
con = sqlite3.connect(db_path)
con.row_factory = sqlite3.Row
cursor = con.cursor()


@dataclass
class Recipe:
    uid: int = 0
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
    thumb_up: int = 0


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
        con.commit()

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

    @classmethod
    def get_with_id(cls, recipe_id: int):
        sql = """
        SELECT * FROM RecipeInfo WHERE id = ?
        """
        cursor.execute(sql, (recipe_id,))
        row = cursor.fetchone()
        if row:
            return Recipe(**row)
        return None
    
    @classmethod
    def get_all_recipe_ids(cls):
        sql = """
        SELECT id FROM RecipeInfo
        """
        cursor.execute(sql)
        return [row[0] for row in cursor.fetchall()]

    @classmethod
    def get_with_offset(cls, offset: int, limit: int):
        sql = """
                SELECT * FROM RecipeInfo
                WHERE uid IN (
                    SELECT MIN(uid) FROM RecipeInfo GROUP BY id
                )
                LIMIT ? OFFSET ?
            """        
        cursor.execute(sql, (limit, offset))
        return [Recipe(**row) for row in cursor.fetchall()]

    @classmethod
    def get_thumbs_up(cls, recipe_id: int):
        sql = """
        SELECT thumb_up FROM RecipeInfo WHERE id = ?
        """
        cursor.execute(sql, (recipe_id,))
        row = cursor.fetchone()
        if row:
            return row[0]
        return 0
    
    @classmethod
    def change_thumbs_up(cls, recipe_id: int, thumbs_up: int):
        sql = """
        UPDATE RecipeInfo SET thumb_up = ? WHERE id = ?
        """
        cursor.execute(sql, (thumbs_up, recipe_id))
        print(f"Recipe ID {recipe_id} thumbs up changed to {thumbs_up}")
        con.commit()
