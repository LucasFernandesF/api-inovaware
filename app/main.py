from fastapi import FastAPI, HTTPException
from app.calculo import tempo_estimado

app = FastAPI()

@app.get("/tempo-estimado") 
def calcular_tempo(distancia_km: float, velocidade_kmh: float):
    """
    Calcula o tempo estimado de uma viagem em minutos.

    Recebe a distância e a velocidade como parâmetros e retorna o tempo total da viagem.
    Levanta um erro 400 se a lógica de negócio falhar.
    """
    try:
        
        tempo = tempo_estimado(distancia_km, velocidade_kmh)
        return {"tempo_estimado_min": tempo}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
