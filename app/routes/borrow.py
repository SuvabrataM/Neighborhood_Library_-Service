from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
prefix="/borrow",
tags=["Borrow Operations"]
)

# ---------------- BORROW BOOK ----------------

@router.post("/", response_model=schemas.BorrowResponse)
def borrow_book(
borrow_data: schemas.BorrowBook,
db: Session = Depends(get_db)
):

    result = crud.borrow_book(db, borrow_data)

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(
        status_code=400,
        detail=result["error"]
    )

    return result

# ---------------- RETURN BOOK ----------------

@router.put("/return/{record_id}",
response_model=schemas.BorrowResponse)
def return_book(
record_id: int,
db: Session = Depends(get_db)
):

    result = crud.return_book(db, record_id)

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(
        status_code=400,
        detail=result["error"]
    )

    return result

# ---------------- MEMBER BORROWED BOOKS ----------------

@router.get("/member/{member_id}",
response_model=list[schemas.BorrowResponse])
def get_member_borrowed_books(
member_id: int,
db: Session = Depends(get_db)
):

    return crud.get_member_borrowed_books(db, member_id)

# ---------------- MEMBER BORROW HISTORY ----------------

@router.get(
"/history/{member_id}",
response_model=list[schemas.BorrowHistoryResponse]
)
def get_member_borrow_history(
member_id: int,
db: Session = Depends(get_db)
):

    return crud.get_member_borrow_history(db, member_id)