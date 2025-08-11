from Functions.flatten_list import flatten_list

def test_flatten():
    nested_list = [[1,2], [3,4,5], [6, 7, 8, 9]]
    esperado = [1,2,3,4,5,6,7,8,9]
    resultado = flatten_list(nested_list)
    assert esperado == resultado
