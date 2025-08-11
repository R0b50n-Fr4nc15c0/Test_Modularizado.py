from Functions.factorial import factorial

def test_factorial():
    n = 0
    esperado = 1
    resultado = factorial(n)
    assert esperado == resultado

def test_factorial_2():
    n = 1
    esperado = 1
    resultado = factorial(n)
    assert esperado == resultado
