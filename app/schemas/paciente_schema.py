from pydantic import BaseModel

class PacienteSchema(BaseModel):
    idPacientes: int
    nombre: str
    rut: str
    edad: int
    sexo: str
    consentimiento: bool

    class Config:
        orm_mode = True