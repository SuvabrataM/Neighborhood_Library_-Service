from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as cr
import app.schemas as sch
from app.database import get_db

router = APIRouter(
prefix="/members",
tags=["Members"]
)

# ---------------- CREATE MEMBER ----------------

@router.post("/", response_model=sch.MemberResponse)
def create_member(
member: sch.MemberCreate,
db: Session = Depends(get_db)
):

    return cr.create_member(db, member)

# ---------------- GET ALL MEMBERS ----------------

@router.get("/", response_model=list[sch.MemberResponse])
def get_members(
db: Session = Depends(get_db)
):

    return cr.get_members(db)

# ---------------- UPDATE MEMBER ----------------

@router.put("/{member_id}", response_model=sch.MemberResponse)
def update_member(
member_id: int,
member: sch.MemberUpdate,
db: Session = Depends(get_db)
):

    updated_member = cr.update_member(db, member_id, member)

    if not updated_member:
        raise HTTPException(
        status_code=404,
        detail="Member not found"
    )

    return updated_member

# ---------------- SEARCH MEMBER BY ID ----------------

@router.get("/search/id/{member_id}",
response_model=sch.MemberResponse)
def search_member_by_id(
member_id: int,
db: Session = Depends(get_db)
):

    member = cr.search_member_by_id(db, member_id)

    if not member:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return member

# ---------------- SEARCH MEMBER BY NAME ----------------

@router.get("/search/name/{name}",
response_model=list[sch.MemberResponse])
def search_member_by_name(
name: str,
db: Session = Depends(get_db)
):

    members = cr.search_member_by_name(db, name)

    if not members:
        raise HTTPException(
            status_code=404,
            detail="No members found"
        )

    return members

# ---------------- SEARCH MEMBER BY PHONE ----------------

@router.get("/search/phone/{phone}",
response_model=list[sch.MemberResponse])
def search_member_by_phone(
phone: str,
db: Session = Depends(get_db)
):

    members = cr.search_member_by_phone(db, phone)

    if not members:
        raise HTTPException(
            status_code=404,
            detail="No members found"
        )

    return members

# ---------------- DELETE MEMBER BY ID ----------------

@router.delete("/delete/id/{member_id}")
def delete_member_by_id(
member_id: int,
db: Session = Depends(get_db)
):

    result = cr.delete_member_by_id(db, member_id)

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Member not found"
        )

    return result

# ---------------- DELETE MEMBER BY NAME ----------------

@router.delete("/delete/name/{name}")
def delete_member_by_name(
name: str,
db: Session = Depends(get_db)
):

    result = cr.delete_member_by_name(db, name)

    if "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result

# ---------------- DELETE MEMBER BY PHONE ----------------

@router.delete("/delete/phone/{phone}")
def delete_member_by_phone(
phone: str,
db: Session = Depends(get_db)
):
    result = cr.delete_member_by_phone(db, phone)

    if "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result
