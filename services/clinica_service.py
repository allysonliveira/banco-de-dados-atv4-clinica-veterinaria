from sqlalchemy.orm import Session
from models.clinica import Clinica
from repositories import clinica_repository
from schemas.clinica_schema import ClinicaCreate

def criar_clinica(db: Session, clinica_data: ClinicaCreate):
    clinica = Clinica(**clinica_data.dict())
    return clinica_repository.criar_clinica(db, clinica)

def listar_clinicas(db: Session):
    return clinica_repository.listar_clinicas(db)

def buscar_clinica_por_id(db: Session, clinica_id: int):
    return clinica_repository.buscar_clinica_por_id(db, clinica_id)