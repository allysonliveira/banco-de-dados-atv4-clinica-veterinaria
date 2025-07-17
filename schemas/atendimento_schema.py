from pydantic import BaseModel
from datetime import datetime

class AtendimentoBase(BaseModel):
    data: datetime
    descricao: str
    pet_id: int
    veterinario_id: int

class AtendimentoCreate(AtendimentoBase):
    pass

class AtendimentoResponse(AtendimentoBase):
    id: int

    class Config:
        orm_mode = True