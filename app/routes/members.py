from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import app.crud as cr
import app.schemas as sch
from app.database import get_db

router = APIRouter(
prefix="/members",
tags=["Members"]
)

@router.post("/", response_model=sch.MemberResponse)
def create_member(member: sch.MemberCreate, db: Session = Depends(get_db)):
    return cr.create_member(db, member)

@router.get("/", response_model=list[sch.MemberResponse])
def get_members(db: Session = Depends(get_db)):
    return cr.get_members(db)

@router.put("/{member_id}", response_model=sch.MemberResponse)
def update_member(member_id: int, member: sch.MemberCreate, db: Session = Depends(get_db)):
    updated_member = cr.update_member(db, member_id, member)

    if not updated_member:
        raise HTTPException(status_code=404, detail="Member not found")

    return updated_member

