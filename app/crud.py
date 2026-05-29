from sqlalchemy.orm import Session

import models
import schemas

# ---------------- BOOK CRUD ----------------
def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def get_books(db: Session):
    return db.query(models.Book).all()

def update_book(db: Session, book_id: int, book: schemas.BookCreate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()

    if not db_book:
        return None

    for key, value in book.dict().items():
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
def update_member(db: Session, member_id: int, member: schemas.MemberCreate):
    db_member = db.query(models.Member).filter(models.Member.id == member_id).first()

    if not db_member:
        return None

    for key, value in member.dict().items():
        setattr(db_member, key, value)

        db.commit()
        db.refresh(db_member)

        return db_member