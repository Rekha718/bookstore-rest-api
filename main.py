from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, database

# Create tables (if not already created)
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="📚 Bookstore REST API")

# Dependency - creates a database session for each request
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------- CRUD ROUTES --------------------

# CREATE Book
@app.post("/books/", response_model=schemas.Book, status_code=201)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

# READ All Books with Filtering + Search
@app.get("/books/", response_model=List[schemas.Book])
def read_books(
    author: str = None,
    genre: str = None,
    price_lt: float = None,
    search: str = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Book)

    # Filtering
    if author:
        query = query.filter(models.Book.author == author)
    if genre:
        query = query.filter(models.Book.genre == genre)
    if price_lt:
        query = query.filter(models.Book.price < price_lt)

    # Search (case-insensitive)
    if search:
        search_term = f"%{search.lower()}%"
        query = query.filter(
            (models.Book.title.ilike(search_term)) |
            (models.Book.author.ilike(search_term)) |
            (models.Book.genre.ilike(search_term))
        )

    return query.all()




# READ One Book by ID
@app.get("/books/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


# UPDATE Book
@app.put("/books/{book_id}", response_model=schemas.Book)
def update_book(book_id: int, updated_book: schemas.BookCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    for key, value in updated_book.dict().items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


# DELETE Book
@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
