from Functions.reverse_string import reverse_string

def test_string_reversa():
    s = "anotaram a data da maratona"
    esperado = "anotaram ad atad a maratona"
    resultado = reverse_string(s)
    assert esperado == resultado
