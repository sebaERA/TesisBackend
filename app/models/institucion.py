from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base

class Institucion(Base):
    __tablename__ = "institucion"

    idinstitucion = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    idtipoinstitucion = Column(Integer, ForeignKey("tipo_institucion.idtipoinstitucion"), nullable=False)