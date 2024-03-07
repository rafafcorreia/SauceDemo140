import pytest

from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros
from utils.utils import ler_csv

# class TestCalculadora():

def test_somar_dois_numeros():

    # Prepara
    num1 = 5
    num2 = 7
    resultado_esperado = 12

    # Executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # Valida
    assert resultado_esperado == resultado_obtido

def test_subtrair_dois_numeros():

    num1 = 30
    num2 = 13
    resultado_esperado = 17

    resultado_obtido = subtrair_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_multiplicar_dois_numeros():

    num1 = 10
    num2 = -5
    resultado_esperado = -50

    resultado_obtido = multiplicar_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros():
    
    num1 = 20
    num2 = 4
    resultado_esperado = 5

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

def test_dividir_dois_numeros_divisor_zero():
    
    num1 = 20
    num2 = 0
    resultado_esperado = 'Erro: Não é possível dividir por zero'

    resultado_obtido = dividir_dois_numeros(num1, num2)

    assert resultado_esperado == resultado_obtido

    """ with pytest.raises(ZeroDivisionError):
        dividir_dois_numeros(num1, num2) """
    
@pytest.mark.parametrize('num1, num2, resultado_esperado',
                          [(8, 3, 11), 
                           (37, 8, 45), 
                           (10, -15, -5)])
def test_somar_dois_numeros_param(num1, num2, resultado_esperado):
    
    resultado_obtido = somar_dois_numeros(num1, num2)
    assert resultado_esperado == resultado_obtido

@pytest.mark.parametrize('num1, num2, resultado_esperado', 
                         ler_csv('C:\\Iterasys\\SauceDemo140\\fixtures\\massaSomar.csv'))
def test_somar_dois_numeros_csv(num1, num2, resultado_esperado):
    
    resultado_obtido = somar_dois_numeros(int(num1), int(num2))
    assert int(resultado_esperado) == resultado_obtido

