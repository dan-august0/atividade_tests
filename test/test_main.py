import pytest

from main import converter_idade, sacar

# Testes para converter_idade
def test_converter_idade_valida():
    assert converter_idade("30") == 30

def test_converter_idade_invalida_texto():
    assert converter_idade("abc") is None

def test_converter_idade_invalida_decimal():
    assert converter_idade("12.5") is None

def test_converter_idade_vazia():
    assert converter_idade("") is None

# Testes para sacar
def test_sacar_valor_positivo():
    assert sacar(100) == 100

def test_sacar_zero():
    assert sacar(0) == 0

def test_sacar_valor_negativo():
    with pytest.raises(ValueError, match="Valor negativo não é permitido"):
        sacar(-10)