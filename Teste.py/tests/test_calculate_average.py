from Functions.calculate_average import calculate_average

#---------Calcular a media-----------

def test_threeint():
    numbers = 6, 8, 7
    esperado = 7
    resultado = calculate_average(numbers)
    assert esperado == resultado

def test_fourint():
    numbers = 4, 7, 9, 9
    esperado = 7.25
    resultado = calculate_average(numbers)
    assert esperado == resultado

def test_int_float_float():
    numbers = 6, 9.5, 8.5
    esperado = 8
    resultado = calculate_average(numbers)
    assert esperado == resultado

