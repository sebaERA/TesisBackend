from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    idpacientes = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    rut = Column(String)
    edad = Column(Integer)
    sexo = Column(String)
    consentimiento = Column(Boolean, default=False)

    idusuarios = Column(Integer, ForeignKey("usuarios.idUsuarios"))
    idasignaciontokens = Column(Integer, ForeignKey("asignacion_tokens.idasignaciontokens"))
    idinstitucion = Column(Integer, ForeignKey("institucion.idinstitucion"))