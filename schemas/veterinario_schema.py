from pydantic import BaseModel

class VeterinarioBase(BaseModel):
    nome: str
    especialidade: str
    clinica_id: int

class VeterinarioCreate(VeterinarioBase):
    pass

class VeterinarioResponse(VeterinarioBase):
    id: int

    class Config:
        orm_mode = True