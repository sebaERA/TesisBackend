from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    idUsuarios = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    idRolUsuario = Column(Integer, ForeignKey("rol_usuario.idRolUsuario"))
    idInstitucion = Column(Integer, ForeignKey("institucion.idInstitucion"))
