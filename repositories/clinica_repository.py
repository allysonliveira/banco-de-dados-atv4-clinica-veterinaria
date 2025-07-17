from sqlalchemy.orm import Session
from models.clinica import Clinica

def criar_clinica(db: Session, clinica: Clinica):
    db.add(clinica)
    db.commit()
    db.refresh(clinica)
    return clinica

def listar_clinicas(db: Session):
    return db.query(Clinica).all()

def buscar_clinica_por_id(db: Session, clinica_id: int):
    return db.query(Clinica).filter(Clinica.id == clinica_id).first()