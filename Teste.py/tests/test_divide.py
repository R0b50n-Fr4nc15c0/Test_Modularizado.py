from Functions.divide import divide

#--------------divisão----------------

def test_divisao():
    a, b = 8, 4
    esperado = 2
    resultado = divide(a, b)
    assert esperado == resultado
