from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.database import Base

class Paciente(Base):
    __tablename__ = "pacientes"

    idPacientes = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    rut = Column(String)
    edad = Column(Integer)
    sexo = Column(String)
    consentimiento = Column(Boolean, default=False)

    idUsuarios = Column(Integer, ForeignKey("usuarios.idUsuarios"))
    idAsignacionTokens = Column(Integer, ForeignKey("asignacion_tokens.idAsignacionTokens"))
    idInstitucion = Column(Integer, ForeignKey("institucion.idInstitucion"))