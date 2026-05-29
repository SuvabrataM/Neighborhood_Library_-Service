from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
prefix="/books",
tags=["Books"]
)

@router.post("/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return crud.create_book(db, book)

@router.get("/", response_model=list[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return crud.get_books(db)

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookCreate, db: Session = Depends(get_db)):
    updated_book = crud.update_book(db, book_id, book)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book