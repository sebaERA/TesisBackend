from pydantic import BaseModel
from datetime import datetime

class ResultadoCreate(BaseModel):
    resultado: str
    idPacientes: int
    idTipoResultado: int

class ResultadoUpdate(BaseModel):
    estado_validacion: str

class ResultadoSchema(BaseModel):
    idResultado: int
    fecha: datetime
    resultado: str
    estado_validacion: str
    idPacientes: int
    idTipoResultado: int

    class Config:
        orm_mode = True
