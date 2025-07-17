from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.clinica_schema import ClinicaCreate, ClinicaResponse
from services import clinica_service
from database import SessionLocal

router = APIRouter(prefix="/clinicas", tags=["Clínicas"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ClinicaResponse)
def criar_clinica(clinica: ClinicaCreate, db: Session = Depends(get_db)):
    return clinica_service.criar_clinica(db, clinica)

@router.get("/", response_model=list[ClinicaResponse])
def listar_clinicas(db: Session = Depends(get_db)):
    return clinica_service.listar_clinicas(db)

@router.get("/{clinica_id}", response_model=ClinicaResponse)
def obter_clinica(clinica_id: int, db: Session = Depends(get_db)):
    clinica = clinica_service.buscar_clinica_por_id(db, clinica_id)
    if not clinica:
        raise HTTPException(status_code=404, detail="Clínica não encontrada")
    return clinica