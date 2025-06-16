def tempo_estimado(distancia_km: float, velocidade_kmh: float) -> float:
    """Calcula o tempo estimado de viagem em minutos

    Args:
        distancia_km (float): _Distancia que será percorrida em quilometros.
        velocidade_kmh (float): Velocidade em quilometros por hora

    Raises:
        ValueError: se a velocidade for menor ou igual a zero

    Returns:
        float: Retorna o tempo estimado em minutos
    """
    if velocidade_kmh <= 0:
        raise ValueError("Velocidade não pode ser menor ou igual a zero")
    return distancia_km / velocidade_kmh * 60
