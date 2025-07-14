from sqlalchemy import Column, Integer, Text, ForeignKey, String, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Resultado(Base):
    __tablename__ = "resultado"

    idresultado = Column(Integer, primary_key=True, index=True)
    fecha = Column(
                            DateTime(timezone=True),
                            server_default=func.now(),
                            nullable=False
                        )
    resultado = Column(Text, nullable=False)
    estado_validacion = Column(String(20), default="pendiente")

    idpacientes = Column(Integer, ForeignKey("pacientes.idpacientes"), nullable=False)
    idtiporesultado = Column(Integer, ForeignKey("tipo_resultado.idtiporesultado"), nullable=False)
