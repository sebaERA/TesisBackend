# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Ahora importamos cada router de su archivo concreto:
from app.routers.paciente      import router as pacientes_router
from app.routers.resultados    import router as resultados_router
from app.routers.usuarios      import router as usuarios_router
from app.routers.evaluacion_api import router as canary_router
from app.models.asignacion_tokens import AsignacionTokens
from app.models.institucion import Institucion
from app.models.tipo_institucion import TipoInstitucion
from app.models.tipo_resultado import TipoResultado



app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Aquí “montamos” cada router con el prefijo que quieras:
app.include_router(pacientes_router,    prefix="/pacientes", tags=["Pacientes"])
app.include_router(resultados_router,   prefix="/resultados", tags=["Resultados"])
app.include_router(usuarios_router,     prefix="/usuarios", tags=["Usuarios"])
app.include_router(canary_router,       prefix="/api", tags=["Canary API"])



@app.get("/")
def read_root():
    return {"mensaje": "Backend ELEAM operativo"
            }
