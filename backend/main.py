from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field
from typing import List
import time

app = FastAPI(
    title="Digital Library API",
    description="Digital Library Application"
)

books: List["Book"] = []

class Book(BaseModel):
    id: int
    title: str = Field(..., min_length=1)
    author: str
    year: int = Field(..., ge=1000, le=2026)
    isbn: str = Field(..., min_length=10, max_length=13)

@app.middleware("http")
async def middleware(request: Request, call_next):
    start = time.time()
    agent = request.headers.get("user-agent")
    print(f"[LOG] Request received from: {agent}")
    response = await call_next(request)
    response.headers["X-Process-Time"] = str(time.time() - start)
    return response

@app.post("/books", tags=["Library"])
def create(book: Book):
    for b in books:
        if b.id == book.id:
            raise HTTPException(status_code=400, detail="Book ID already exists")
    books.append(book)
    return book

@app.get("/books", tags=["Library"])
def read_all():
    return books

@app.get("/books/{id}", tags=["Library"])
def read(id: int):
    for b in books:
        if b.id == id:
            return b
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{id}", tags=["Library"])
def update(id: int, book: Book):
    for i in range(len(books)):
        if books[i].id == id:
            books[i] = book
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{id}", tags=["Library"])
def delete(id: int):
    for b in books:
        if b.id == id:
            books.remove(b)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")