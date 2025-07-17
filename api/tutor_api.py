from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.tutor_schema import TutorCreate, TutorResponse
from models.tutor import Tutor

router = APIRouter(prefix="/tutores", tags=["Tutores"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TutorResponse)
def criar_tutor(tutor: TutorCreate, db: Session = Depends(get_db)):
    novo = Tutor(**tutor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo