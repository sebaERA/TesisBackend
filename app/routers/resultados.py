from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.resultado import Resultado
from app.schemas.resultado_schema import ResultadoCreate, ResultadoSchema, ResultadoUpdate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/{paciente_id}", response_model=List[ResultadoSchema])
def obtener_resultados_por_paciente(paciente_id: int, db: Session = Depends(get_db)):
    return db.query(Resultado).filter(Resultado.idPacientes == paciente_id).all()

@router.post("/", response_model=ResultadoSchema)
def registrar_resultado(data: ResultadoCreate, db: Session = Depends(get_db)):
    nuevo = Resultado(**data.dict())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@router.put("/{id_resultado}", response_model=ResultadoSchema)
def actualizar_estado_resultado(id_resultado: int, data: ResultadoUpdate, db: Session = Depends(get_db)):
    resultado = db.query(Resultado).filter(Resultado.idResultado == id_resultado).first()
    if not resultado:
        raise HTTPException(status_code=404, detail="Resultado no encontrado")
    resultado.estado_validacion = data.estado_validacion
    db.commit()
    db.refresh(resultado)
    return resultado
