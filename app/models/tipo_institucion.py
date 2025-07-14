from sqlalchemy import Column, Integer, String
from app.database import Base

class TipoInstitucion(Base):
    __tablename__ = 'tipo_institucion'
    idtipoinstitucion = Column(Integer, primary_key=True)
    descripcion = Column(String)
