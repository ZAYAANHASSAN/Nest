# app/routes/class_routes.py
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models import Class
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/classes")
def create_class(name: str, db: Session = Depends(get_db)):
    new_class = Class(name=name)
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    return new_class
