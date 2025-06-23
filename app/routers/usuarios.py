from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from datetime import timedelta

from app.database import SessionLocal
from app.models.usuario import Usuario
from app.schemas.usuario_schema import UsuarioSchema, UsuarioLogin, UsuarioCreate
from app.services.auth import (
    get_db,
    verify_password,
    get_password_hash,
    create_access_token,
    get_current_user
)

router = APIRouter()

@router.get("/", response_model=List[UsuarioSchema])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales inválidas")

    token = create_access_token(data={"sub": user.email}, expires_delta=timedelta(minutes=60))
    return {"access_token": token, "token_type": "bearer"}

@router.post("/registro", response_model=UsuarioSchema)
def registrar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Validar si ya existe
    if db.query(Usuario).filter(Usuario.email == usuario.email).first():
        raise HTTPException(status_code=400, detail="El correo ya está registrado")

    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        password=get_password_hash(usuario.password),
        idRolUsuario=usuario.idRolUsuario,
        idInstitucion=usuario.idInstitucion
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/perfil")
def obtener_perfil(usuario: Usuario = Depends(get_current_user)):
    return {"nombre": usuario.nombre, "email": usuario.email}
