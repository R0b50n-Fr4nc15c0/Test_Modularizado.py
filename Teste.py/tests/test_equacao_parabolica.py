from Functions.equacao_parabolica import equacao_parabolica

def test_equacao_parabolica_resultado_complexo():
    a, b, c = 1, 2, 5  # delta < 0 → raízes complexas
    resultado = equacao_parabolica(a, b, c)
    esperado = (
        complex(-1, 2),
        complex(-1, -2)
    )
    assert resultado == esperado