from datetime import datetime

from sqlalchemy.orm import Session

from app import models, schemas

# ---------------- BOOK CRUD ----------------

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def get_books(db: Session):
    return db.query(models.Book).all()


def update_book(
db: Session,
book_id: int,
book_data: schemas.BookUpdate
):
    db_book = db.query(models.Book).filter(
    models.Book.id == book_id
).first()

    if not db_book:
        return None

    update_data = book_data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)

    return db_book


# ---------------- MEMBER CRUD ----------------

def create_member(db: Session, member: schemas.MemberCreate):

    db_member = models.Member(**member.dict())

    db.add(db_member)
    db.commit()
    db.refresh(db_member)

    return db_member


def get_members(db: Session):

    return db.query(models.Member).all()


def update_member(
db: Session,
member_id: int,
member_data: schemas.MemberUpdate
):

    db_member = db.query(models.Member).filter(
    models.Member.id == member_id
).first()

    if not db_member:
        return None

    update_data = member_data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_member, key, value)

    db.commit()
    db.refresh(db_member)

    return db_member

# ---------------- BORROW BOOK ----------------

def borrow_book(db: Session, borrow_data: schemas.BorrowBook):

    member = db.query(models.Member).filter(
    models.Member.id == borrow_data.member_id
).first()

    if not member:
        return {"error": "Member not found"}

    book = db.query(models.Book).filter(
         models.Book.id == borrow_data.book_id
         ).first()

    if not book:
        return {"error": "Book not found"}

    if book.available_copies <= 0:
        return {"error": "Book is not available"}

    borrow_record = models.BorrowRecord(
    member_id=borrow_data.member_id,
    book_id=borrow_data.book_id
)

    book.available_copies -= 1

    db.add(borrow_record)
    db.commit()
    db.refresh(borrow_record)

    return borrow_record

# ---------------- RETURN BOOK ----------------

def return_book(db: Session, record_id: int):

    borrow_record = db.query(models.BorrowRecord).filter(
    models.BorrowRecord.id == record_id
).first()

    if not borrow_record:
        return {"error": "Borrow record not found"}

    if borrow_record.returned_at:
        return {"error": "Book already returned"}

    borrow_record.returned_at = datetime.utcnow()

    book = db.query(models.Book).filter(
    models.Book.id == borrow_record.book_id
).first()

    book.available_copies += 1

    db.commit()
    db.refresh(borrow_record)

    return borrow_record

# ---------------- MEMBER BORROWED BOOKS ----------------

def get_member_borrowed_books(db: Session, member_id: int):

    borrowed_books = db.query(models.BorrowRecord).filter(
    models.BorrowRecord.member_id == member_id,
    models.BorrowRecord.returned_at == None
).all()

    return borrowed_books

# ---------------- MEMBER BORROW HISTORY ----------------
def get_member_borrow_history(db: Session, member_id: int):

    history = db.query(models.BorrowRecord).filter(
    models.BorrowRecord.member_id == member_id
).all()

    return history