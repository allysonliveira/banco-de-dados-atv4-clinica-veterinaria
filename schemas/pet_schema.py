from pydantic import BaseModel

class PetBase(BaseModel):
    nome: str
    especie: str
    idade: int
    tutor_id: int

class PetCreate(PetBase):
    pass

class PetResponse(PetBase):
    id: int

    class Config:
        orm_mode = True