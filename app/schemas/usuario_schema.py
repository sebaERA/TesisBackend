from pydantic import BaseModel

class UsuarioLogin(BaseModel):
    email: str
    password: str

class UsuarioCreate(BaseModel):
    nombre: str
    email: str
    password: str
    idRolUsuario: int
    idInstitucion: int

class UsuarioSchema(BaseModel):
    idUsuarios: int
    nombre: str
    email: str

    class Config:
        orm_mode = True