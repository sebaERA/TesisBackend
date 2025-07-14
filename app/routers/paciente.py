from fastapi import APIRouter, Depends, Body, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.paciente import Paciente
from app.schemas.paciente_schema import PacienteSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[PacienteSchema])
def listar_pacientes(db: Session = Depends(get_db)):
    print(">>> PACIENTES EN BD:", db.query(Paciente).all())
    # ---------------------------------
    return db.query(Paciente).all()

@router.put("/{id}/consentimiento", response_model=PacienteSchema)
def actualizar_consentimiento(id: int, estado: bool = Body(...), db: Session = Depends(get_db)):
    paciente = db.query(Paciente).filter(Paciente.idpacientes == id).first()
    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")
    
    paciente.consentimiento = estado
    db.commit()
    db.refresh(paciente)
    return paciente