from fastapi import APIRouter, UploadFile, File, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.canary_api import analizar_audio
from app.models.resultado import Resultado
import os
import uuid

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/evaluar-audio")
async def evaluar_audio(
    file: UploadFile = File(...),
    idPaciente: int = Form(...),
    idTipoResultado: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        # 1. Guardar temporalmente el archivo
        filename = f"temp_{uuid.uuid4()}.wav"
        with open(filename, "wb") as f:
            f.write(await file.read())

        # 2. Analizar el audio
        scores = analizar_audio(filename)

        # 3. Eliminar el archivo temporal
        os.remove(filename)

        # 4. Extraer texto de resultado
        texto_resultado = ", ".join(
            f"{s['code']}: {s['data']['result']}" for s in scores
        )

        # 5. Guardar en base de datos
        nuevo_resultado = Resultado(
            resultado=texto_resultado,
            idPacientes=idPaciente,
            idTipoResultado=idTipoResultado
        )
        db.add(nuevo_resultado)
        db.commit()
        db.refresh(nuevo_resultado)

        return {
            "mensaje": "Resultado registrado correctamente",
            "resultado": texto_resultado,
            "idResultado": nuevo_resultado.idResultado
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en análisis: {e}")

