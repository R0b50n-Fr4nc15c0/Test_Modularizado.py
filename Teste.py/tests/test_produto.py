from Functions.produto import produto

# --------Produto(multiplicação)--------
def test_produto_int():
    a, b = 4, 7
    resultadoEsperado = 28
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_int_float():
    a, b = 5, 1.94
    resultadoEsperado = 9.70
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_int_string():
    a, b = 9, "11"
    resultadoEsperado = 99
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_string_int():
    a, b = "9", 6
    resultadoEsperado = 54
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_int_floatstring():
    a, b = 3, "12.99"
    resultadoEsperado = 38.97
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_floastring_int():
    a, b = "5.79", 4
    resultadoEsperado = 23.16
    resultado = produto(a, b)
    assert resultado == resultadoEsperado

def test_produto_string_float():
    a, b = "3", 11.49
    resultadoEsperado = 34.47
    resultado = produto(a, b)
    assert resultado == resultadoEsperado
