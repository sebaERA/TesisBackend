# Usa una imagen base oficial de Python (ajusta la versión si es necesario)
FROM python:3.12-slim

WORKDIR /app

# Copia solo el requirements.txt primero para aprovechar el cache de Docker
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Ahora copia el resto del código fuente
COPY . .

# Exponer el puerto 8080 (Cloud Run estándar)
EXPOSE 8080

# Variable de entorno estándar de Cloud Run
ENV PORT=8080

# Comando para iniciar FastAPI (ajusta si tu archivo principal NO es main.py)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
