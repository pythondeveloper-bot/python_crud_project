import sqlite3

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("create table students(id INTEGER PRIMARY KEY AUTOINCREMENT ,name TEXT,marks INTEGER)")

conn.commit()
conn.close()

print("db created successfully")