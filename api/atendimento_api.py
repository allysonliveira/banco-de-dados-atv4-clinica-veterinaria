from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.atendimento_schema import AtendimentoCreate, AtendimentoResponse
from models.atendimento import Atendimento

router = APIRouter(prefix="/atendimentos", tags=["Atendimentos"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AtendimentoResponse)
def criar_atendimento(a: AtendimentoCreate, db: Session = Depends(get_db)):
    novo = Atendimento(**a.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[AtendimentoResponse])
def listar_atendimentos(db: Session = Depends(get_db)):
    return db.query(Atendimento).all()