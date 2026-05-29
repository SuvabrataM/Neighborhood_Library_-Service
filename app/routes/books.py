from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.database import get_db

router = APIRouter(
prefix="/books",
tags=["Books"]
)

# ---------------- CREATE BOOK ----------------

@router.post("/", response_model=schemas.BookResponse)
def create_book(
book: schemas.BookCreate,
db: Session = Depends(get_db)
):
    return crud.create_book(db, book)

# ---------------- GET ALL BOOKS ----------------

@router.get("/", response_model=list[schemas.BookResponse])
def get_books(
db: Session = Depends(get_db)
):

    return crud.get_books(db)

# ---------------- UPDATE BOOK ----------------

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(
book_id: int,
book: schemas.BookUpdate,
db: Session = Depends(get_db)
):

    updated_book = crud.update_book(db, book_id, book)

    if not updated_book:
        raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

    return updated_book

# ---------------- SEARCH BY ID ----------------

# ---------------- SEARCH BY ID ----------------

@router.get("/search/id/{book_id}",
response_model=schemas.BookResponse)
def search_book_by_id(
book_id: int,
db: Session = Depends(get_db)
):

    query = db.query(models.Book).filter(
    models.Book.id == book_id,
    models.Book.is_deleted == False
    ).first()

    if not query:
        raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

    return query


# ---------------- SEARCH BY TITLE ----------------

@router.get("/search/title/{title}",
response_model=schemas.BookResponse)
def search_book_by_title(
title: str,
db: Session = Depends(get_db)
):

    query = db.query(models.Book).filter( models.Book.title.ilike(f"%{title}%"),
            models.Book.is_deleted == False ).first()

    if not query:
        raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

    return query

# ---------------- SEARCH BY AUTHOR ----------------

@router.get("/search/author/{author}",
response_model=list[schemas.BookResponse])
def search_books_by_author(
author: str,
db: Session = Depends(get_db)
):
    books = db.query(models.Book).filter( models.Book.author.ilike(f"%{author}%")
            , models.Book.is_deleted == False ).all()

    if not books:
        raise HTTPException(
        status_code=404,
        detail="No books found"
    )

    return books

# ---------------- DELETE BOOK BY ID ----------------

@router.delete("/delete/id/{book_id}")
def delete_book_by_id(
book_id: int,
db: Session = Depends(get_db)
):


    result = crud.delete_book_by_id(db, book_id)

    if not result:
        raise HTTPException(
        status_code=404,
        detail="Book not found"
    )

    return result

# ---------------- DELETE BOOK BY TITLE ----------------

@router.delete("/delete/title/{title}")
def delete_book_by_title(
title: str,
db: Session = Depends(get_db)
):
    result = crud.delete_book_by_title(db, title)

    if "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result

# ---------------- DELETE BOOK BY AUTHOR ----------------

@router.delete("/delete/author/{author}")
def delete_books_by_author(
author: str,
db: Session = Depends(get_db)
):

    result = crud.delete_books_by_author(db, author)

    if "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result