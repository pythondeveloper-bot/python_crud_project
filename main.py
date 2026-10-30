import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.post("/students")
def student():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    cursor.execute("select * from students")

    conn.commit()
    conn.close()

    return {"message": "Students viewed successfully"}
