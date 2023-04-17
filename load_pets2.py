import sqlite3
connection = sqlite3.connect("pets.db")

cursor = connection.cursor()
# cursor.execute()

with open('pets.sql', 'r') as f:
    sql = f.read()
cursor.executescript(sql)
connection.commit()
connection.close()