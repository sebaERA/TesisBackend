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
    idpacientes: int = Form(...),
    idtiporesultado: int = Form(...),
    db: Session = Depends(get_db)
):
    try:
        print("Inicio evaluar_audio")  # <-- LOG A
        filename = f"temp_{uuid.uuid4()}.wav"
        with open(filename, "wb") as f:
            f.write(await file.read())
        print("Archivo guardado")  # <-- LOG B

        scores = analizar_audio(filename)
        print(f"Audio analizado: {scores}")  # <-- LOG C

        os.remove(filename)
        print("Archivo temporal eliminado")  # <-- LOG D

        texto_resultado = ", ".join(
            f"{s['code']}: {s['data']['result']}" for s in scores
        )
        print(f"Texto resultado generado: {texto_resultado}")  # <-- LOG E

        nuevo_resultado = Resultado(
            resultado=texto_resultado,
            idpacientes=idpacientes,
            idtiporesultado=idtiporesultado
        )
        db.add(nuevo_resultado)
        db.commit()
        db.refresh(nuevo_resultado)
        print("Resultado guardado en base de datos")  # <-- LOG F

        return {
            "mensaje": "Resultado registrado correctamente",
            "resultado": texto_resultado,
            "idresultado": nuevo_resultado.idresultado
        }

    except Exception as e:
        print(f"ERROR EN /evaluar-audio: {e}")  # LOG DE ERROR
        raise HTTPException(status_code=500, detail=f"Error en análisis: {e}")
