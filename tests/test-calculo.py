import pytest
from app.calculo import tempo_estimado

def test_tempo_normal():
    assert tempo_estimado(60, 60) == 60.0

def test_tempo_lento():
    assert tempo_estimado(30, 30) == 60.0

def test_velocidade_zero():
    with pytest.raises(ValueError):
        tempo_estimado(10, 0)
