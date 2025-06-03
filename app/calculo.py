def tempo_estimado(distancia_km: float, velocidade_kmh: float) -> float:
    if velocidade_kmh == 0:
        raise ValueError("Velocidade não pode ser zero")
    return distancia_km / velocidade_kmh * 60  # retorna minutos
