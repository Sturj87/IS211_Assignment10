import sqlite3
connection = sqlite3.connect("music.db")

cursor = connection.cursor()
# cursor.execute()

with open('music.sql', 'r') as f:
    sql = f.read()
cursor.executescript(sql)
connection.commit()
connection.close()