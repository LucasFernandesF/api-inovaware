from fastapi import FastAPI, HTTPException
from app.calculo import tempo_estimado

app = FastAPI()

@app.get("/tempo-estimado")
def calcular_tempo(distancia_km: float, velocidade_kmh: float):
    try:
        tempo = tempo_estimado(distancia_km, velocidade_kmh)
        return {"tempo_estimado_min": tempo}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
