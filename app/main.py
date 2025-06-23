# backend_api/app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pacientes, evaluaciones,evaluacion_api

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pacientes.router, prefix="/pacientes", tags=["Pacientes"])
app.include_router(evaluaciones.router, prefix="/evaluaciones", tags=["Evaluaciones"])
app.include_router(evaluacion_api.router, prefix="/api", tags=["Canary API"])

@app.get("/")
def read_root():
    return {"mensaje": "Backend ELEAM operativo"}