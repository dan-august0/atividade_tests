import pytest
import os
import json
from main import salvar_pontuacao

# Testes para converter_idade
def test_converter_idade_valida():
    salvar_pontuacao('Mari', 100, 'pontuacoes-test.json')

    with open("pontuacoes-test.json", "r") as arquivo:
        pontuacoes = json.load(arquivo)

    assert len(pontuacoes) == 1
    assert pontuacoes[0]['nome'] == 'Mari'

    # conftest
    os.remove('pontuacoes-test.json')



'''def test_converter_idade_invalida_texto():
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
        sacar(-10)'''