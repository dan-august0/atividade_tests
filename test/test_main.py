import pytest

from main import soma, dividir

# Testes para a função soma
def test_soma_positivos():
    assert soma(2, 3) == 5

def test_soma_negativo_e_positivo():
    assert soma(-1, 1) == 0

# Testes para a função dividir
def test_dividir_valores_validos():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(5, 0)