from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from schemas.pet_schema import PetCreate, PetResponse
from models.pet import Pet

router = APIRouter(prefix="/pets", tags=["Pets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=PetResponse)
def criar_pet(pet: PetCreate, db: Session = Depends(get_db)):
    novo = Pet(**pet.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.get("/", response_model=list[PetResponse])
def listar_pets(db: Session = Depends(get_db)):
    return db.query(Pet).all()