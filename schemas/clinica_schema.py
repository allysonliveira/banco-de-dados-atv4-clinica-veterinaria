from pydantic import BaseModel

class ClinicaBase(BaseModel):
    nome: str
    cidade: str

class ClinicaCreate(ClinicaBase):
    pass

class ClinicaResponse(ClinicaBase):
    id: int

    class Config:
        orm_mode = True