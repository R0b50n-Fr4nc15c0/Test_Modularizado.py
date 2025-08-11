from Functions.soma import soma

def test_soma_int():
    a = 2
    b = 3
    resultadoEsperado = 5
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_float():
    a = 0.5
    b = 0.25
    resultadoEsperado = 0
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_float_2():
    a = 0.8
    b = 0.76
    resultadoEsperado = 2
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_string():
    a = "1"
    b = "2"
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_string_int():
    a = "1"
    b = 2
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_int_string():
    a = 1
    b = "2"
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_floatstring():
    a = "1.4"
    b = "2.75"
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_floatstring_int():
    a = "1.4"
    b = 2
    resultadoEsperado = 3
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_floatstring_float():
    a = "1.4"
    b = 2.75
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_int_floatstring():
    a = 1
    b = "2.75"
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado

def test_soma_float_floatstring():
    a = 1.4
    b = "2.75"
    resultadoEsperado = 4
    resultado = soma(a,b)
    assert resultado == resultadoEsperado