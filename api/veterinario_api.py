from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.veterinario_schema import VeterinarioCreate, VeterinarioResponse
from models.veterinario import Veterinario

router = APIRouter(prefix="/veterinarios", tags=["Veterinários"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=VeterinarioResponse)
def criar_veterinario(vet: VeterinarioCreate, db: Session = Depends(get_db)):
    novo = Veterinario(**vet.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[VeterinarioResponse])
def listar_veterinarios(db: Session = Depends(get_db)):
    return db.query(Veterinario).all()