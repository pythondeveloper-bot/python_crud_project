# Student Management REST API

A backend REST API built using **Python**, **FastAPI**, and **SQLite** to perform CRUD operations non student records.

## Tech Stack
- Python 3
- FastAPI
- SQLite
- Uvicorn & SwaggerUI

# Features
- Create, read, update, and delete student records
- Interactive API documentation and endpoint testing using Swagger UI
- Lightweight SQLite database integration

# How to Run Locally
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn

2. Initialize the database:
   bash
   python create_db.py

3. Start the FastAPI server:
   bash
   uvicorn main:app --reload

4. Open Swagger UI in your browser:
   http://127.0.0.1:8000/docs
