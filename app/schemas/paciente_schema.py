from pydantic import BaseModel

class PacienteSchema(BaseModel):
    idpacientes: int
    nombre: str
    rut: str
    edad: int
    sexo: str
    consentimiento: bool
    idusuarios: int
    idasignaciontokens: int
    idinstitucion: int

    class Config:
        orm_mode = True