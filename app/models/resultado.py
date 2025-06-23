from sqlalchemy import Column, Integer, Text, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Resultado(Base):
    __tablename__ = "resultado"

    idResultado = Column(Integer, primary_key=True, index=True)
    fecha = Column(DateTime(timezone=True), server_default=func.now())
    resultado = Column(Text, nullable=False)
    estado_validacion = Column(String(20), default="pendiente")

    idPacientes = Column(Integer, ForeignKey("pacientes.idPacientes"), nullable=False)
    idTipoResultado = Column(Integer, ForeignKey("tipo_resultado.idTipoResultado"), nullable=False)
