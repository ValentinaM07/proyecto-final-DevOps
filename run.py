
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(
    title="API de Ventas",
    description="API para gestión de clientes, productos y ventas",
    version="1.0.0"
)

# Endpoint básico para prueba
@app.get("/")
def read_root():
    return {"message": "API corriendo correctamente 🚀"}

# Configurar Prometheus para exponer métricas en /metrics
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

import uvicorn
from app import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)

