def tempo_estimado(distancia_km: float, velocidade_kmh: float) -> float:
    if velocidade_kmh <= 0:
        raise ValueError("A velocidade deve ser maior que 0 km/h.")
    return round(distancia_km / velocidade_kmh * 60, 2)
