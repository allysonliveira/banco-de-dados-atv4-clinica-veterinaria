from pydantic import BaseModel

class TutorBase(BaseModel):
    nome: str
    telefone: str

class TutorCreate(TutorBase):
    pass

class TutorResponse(TutorBase):
    id: int

    class Config:
        orm_mode = True