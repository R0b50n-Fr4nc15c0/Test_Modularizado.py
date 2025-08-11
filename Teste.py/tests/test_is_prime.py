from Functions.is_prime import is_prime

#--------Numero primo--------

def test_N_Primo():
    n = 5
    esperado = True
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo2():
    n = 9
    esperado = True
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo3():
    n = -4
    esperado = False
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo4():
    n = 0
    esperado = False
    resultado = is_prime(n)
    assert esperado == resultado

def test_N_Primo5():
    n = 27
    esperado = False
    resultado = is_prime(n)
    assert esperado == resultado
