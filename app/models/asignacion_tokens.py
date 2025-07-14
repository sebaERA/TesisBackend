from sqlalchemy import Column, Integer, String
from app.database import Base

class AsignacionTokens(Base):
    __tablename__ = 'asignacion_tokens'
    idasignaciontokens = Column(Integer, primary_key=True)
    token = Column(String)
    fecha_expiracion = Column(String)
