from pydantic import BaseModel
from datetime import datetime

class ResultadoCreate(BaseModel):
    resultado: str
    idpacientes: int
    idtiporesultado: int

class ResultadoUpdate(BaseModel):
    estado_validacion: str

class ResultadoSchema(BaseModel):
    idresultado: int
    fecha: datetime
    resultado: str
    estado_validacion: str
    idpacientes: int
    idtiporesultado: int

    class Config:
        orm_mode = True
