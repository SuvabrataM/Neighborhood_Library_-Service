from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as cr
import app.schemas as sch
from app.database import get_db

router = APIRouter(
prefix="/books",
tags=["Books"]
)

@router.post("/", response_model=sch.BookResponse)
def create_book(book: sch.BookCreate, db: Session = Depends(get_db)):
    return cr.create_book(db, book)

@router.get("/", response_model=list[sch.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return cr.get_books(db)

@router.put("/{book_id}", response_model=sch.BookResponse)
def update_book(book_id: int, book: sch.BookCreate, db: Session = Depends(get_db)):
    updated_book = cr.update_book(db, book_id, book)

    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return updated_book