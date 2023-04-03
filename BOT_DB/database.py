import sqlite3
import random


def sql_create():
    global db, cursor
    db = sqlite3.connect("cinemabot.sqlite3")
    cursor = db.cursor()

    if db:
        print("db connected!")

    db.execute("CREATE TABLE IF NOT EXISTS films "
               "(id INTEGER PRIMARY KEY, "
               "title VARCHAR (100), "
               "caption VARCHAR (100), "
               "link VARCHAR(100))")
    db.commit()


sql_create()