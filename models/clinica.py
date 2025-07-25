from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models import Base

class Clinica(Base):
    __tablename__ = "clinicas"

    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    cidade = Column(String, nullable=False)

    veterinarios = relationship("Veterinario", back_populates="clinica")