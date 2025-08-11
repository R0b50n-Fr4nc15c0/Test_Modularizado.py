from Functions.authenticate_user import authenticate_user

def test_Autenticar():
    username, password = "admin", "1234"
    esperado = True
    resultado = authenticate_user(username, password)
    assert esperado == resultado