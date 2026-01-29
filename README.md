# FastAPI Digital Library

This is a simple Digital Library application built using FastAPI.

The application provides REST APIs to manage books in a library.
This project is created as part of the Week 3 assignment.

---

## Project Structure

fastapi-digital-library/
├── backend/
│   └── main.py
├── requirements.txt
├── README.md

---

## How to Run the Project

### Step 1: Create virtual environment
python -m venv .venv

### Step 2: Activate virtual environment (Windows)
.venv\Scripts\activate

### Step 3: Install required packages
pip install fastapi uvicorn

### Step 4: Run the application
uvicorn backend.main:app --reload

---

## Swagger Documentation

After running the server, open the following URL in browser:

http://127.0.0.1:8000/docs

---

## Book Model

Each book has the following fields:
id  
title  
author  
year  
isbn  

Validation rules:
- title should not be empty
- year should be between 1000 and 2026
- isbn should be 10 or 13 characters

---

## Available APIs

POST   /books        → Add a new book  
GET    /books        → Get all books  
GET    /books/{id}   → Get book by ID  
PUT    /books/{id}   → Update book  
DELETE /books/{id}   → Delete book  

All APIs are grouped under the Library tag.

---

## Error Handling

- Duplicate book ID returns 400 error
- Book not found returns 404 error
- Invalid data returns validation error

---

## Middleware

For every request:
- User-Agent is printed in console
- Request processing time is added in response header

---

## Notes

- Uses in-memory storage
- No database is used
- This project is for learning purpose

---

## License

This project uses the MIT License.