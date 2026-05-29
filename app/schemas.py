from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ---------------- BOOK SCHEMAS ----------------

class BookBase(BaseModel):
    title: str
    author: str
    isbn: Optional[str] = None
    total_copies: int
    available_copies: int

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    isbn: Optional[str] = None
    total_copies: Optional[int] = None
    available_copies: Optional[int] = None

class BookResponse(BookBase):
    id: int
    class Config:
        orm_mode = True


# ---------------- MEMBER SCHEMAS ----------------

class MemberBase(BaseModel):
    name: str
    email: str
    phone: Optional[str] = None

class MemberCreate(MemberBase):
    pass

class MemberUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None

class MemberResponse(MemberBase):
    id: int

    class Config:
        orm_mode = True


# ---------------- BORROW SCHEMAS ----------------

class BorrowBook(BaseModel):
    member_id: int
    book_id: int

class BorrowResponse(BaseModel):
    id: int
    member_id: int
    book_id: int
    borrowed_at: datetime
    returned_at: Optional[datetime]

    class Config:
        orm_mode = True

