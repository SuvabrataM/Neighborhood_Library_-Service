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
    return db.query(models.Book).filter(
    models.Book.is_deleted == False
    ).all()


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

    return db.query(models.Member).filter(
    models.Member.is_deleted == False
    ).all()


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
        models.Member.id == borrow_data.member_id,
        models.Member.is_deleted == False
    ).first()

    if not member:
        return {"error": "Member not found"}

    book = db.query(models.Book).filter(
        models.Book.id == borrow_data.book_id,
        models.Book.is_deleted == False
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

    result = []

    for record in borrowed_books:

        result.append({
        "id": record.id,
        "member_id": record.member_id,
        "book_id": record.book_id,
        "book_title": record.book.title,
        "borrowed_at": record.borrowed_at,
        "returned_at": record.returned_at
    })

    return result

# ---------------- MEMBER BORROW HISTORY ----------------
def get_member_borrow_history(db: Session, member_id: int):

    history = db.query(models.BorrowRecord).filter(
    models.BorrowRecord.member_id == member_id
    ).all()

    result = []

    for record in history:
        result.append({
        "id": record.id,
        "member_id": record.member_id,
        "book_id": record.book_id,
        "book_title": record.book.title,
        "borrowed_at": record.borrowed_at,
        "returned_at": record.returned_at
    })

    return result

# ---------------- SEARCH BOOKS ----------------

def search_book_by_id(db: Session, book_id: int):
    return db.query(models.Book).filter(
        models.Book.id == book_id,
        models.Book.is_deleted == False
    ).first()

def search_book_by_title(db: Session, title: str):
    return db.query(models.Book).filter(
        models.Book.title.ilike(f"%{title}%"),
        models.Book.is_deleted == False
    ).first()

def search_books_by_author(db: Session, author: str):
    return db.query(models.Book).filter(
        models.Book.author.ilike(f"%{author}%"),
        models.Book.is_deleted == False
    ).all()

# ---------------- DELETE BOOK ----------------

def delete_book_by_id(db: Session, book_id: int):

    book = db.query(models.Book).filter(
        models.Book.id == book_id,
        models.Book.is_deleted == False
    ).first()

    if not book:
        return {"error": "Book not found or already deleted"}

    book.is_deleted = True

    db.commit()

    return {"message": "Book deleted successfully"}

def delete_book_by_title(db: Session, title: str):

    books = db.query(models.Book).filter(
        models.Book.title.ilike(f"%{title}%"),
        models.Book.is_deleted == False
    ).all()

    if not books:
        return {"error": "Book not found or already deleted"}

    for book in books:
        book.is_deleted = True

    db.commit()

    return {"message": "Book(s) deleted successfully"}

def delete_books_by_author(db: Session, author: str):

    books = db.query(models.Book).filter(
        models.Book.author.ilike(f"%{author}%"),
        models.Book.is_deleted == False
    ).all()

    if not books:
        return {"error": "Book not found or already deleted"}

    for book in books:
        book.is_deleted = True

    db.commit()

    return {"message": "Book(s) deleted successfully"}

# ---------------- SEARCH MEMBERS ----------------

def search_member_by_id(db: Session, member_id: int):


    return db.query(models.Member).filter(
        models.Member.id == member_id,
        models.Member.is_deleted == False
    ).first()

def search_member_by_name(db: Session, name: str):


    return db.query(models.Member).filter(
        models.Member.name.ilike(f"%{name}%"),
        models.Member.is_deleted == False
    ).all()

def search_member_by_phone(db: Session, phone: str):

    return db.query(models.Member).filter(
        models.Member.phone == phone,
        models.Member.is_deleted == False
    ).all()

# ---------------- DELETE MEMBER ----------------

def delete_member_by_id(db: Session, member_id: int):

    member = db.query(models.Member).filter(
        models.Member.id == member_id,
        models.Member.is_deleted == False
    ).first()

    if not member:
        return {"error": "Member not found or already deleted"}

    member.is_deleted = True

    db.commit()

    return {"message": "Member deleted successfully"}

def delete_member_by_name(db: Session, name: str):

    members = db.query(models.Member).filter(
        models.Member.name.ilike(f"%{name}%"),
        models.Member.is_deleted == False
    ).all()

    if not members:
        return {"error": "Member not found or already deleted"}

    for member in members:
        member.is_deleted = True

    db.commit()

    return {"message": "Member(s) deleted successfully"}

def delete_member_by_phone(db: Session, phone: str):

    members = db.query(models.Member).filter(
        models.Member.phone == phone,
        models.Member.is_deleted == False
    ).all()

    if not members:
        return {"error": "Member not found or already deleted"}

    for member in members:
        member.is_deleted = True

    db.commit()

    return {"message": "Member(s) deleted successfully"}