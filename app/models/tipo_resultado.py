from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoResultado(Base):
    __tablename__ = 'tipo_resultado'
    idtiporesultado = Column(Integer, primary_key=True)
    descripcion = Column(String)
