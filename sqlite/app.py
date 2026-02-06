import sqlite3
import json
from pathlib import Path

movies = json.loads(Path("../json/movies.json").read_text())
# print(movies)

with sqlite3.connect("db.sqlite3") as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT,
            year INTEGER,
            director TEXT,
            genre TEXT
        )
        """
    )

    # for movie in movies:
    #     cursor.execute(
    #         """
    #         INSERT INTO movies (id, title, year, director, genre)
    #         VALUES (?, ?, ?, ?, ?)
    #         """,
    #         (movie["id"], movie["title"], movie["year"],
    #          movie["director"], movie["genre"])
    #     )

    # conn.commit()

    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
