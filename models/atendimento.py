from sqlalchemy import Column, Integer, DateTime, String, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class Atendimento(Base):
    __tablename__ = "atendimentos"

    id = Column(Integer, primary_key=True)
    data = Column(DateTime, nullable=False)
    descricao = Column(String, nullable=False)
    pet_id = Column(Integer, ForeignKey("pets.id"))
    veterinario_id = Column(Integer, ForeignKey("veterinarios.id"))

    pet = relationship("Pet", back_populates="atendimentos")
    veterinario = relationship("Veterinario", back_populates="atendimentos")