from Functions.read_file_content import read_file_content

#------------Ler arquivo------------

def test_read_file(tmp_path):
    test_file = tmp_path / "teste.txt"
    esperado = "Boa tarde fulano."
    test_file.write_text(esperado,encoding="utf-8")
    resultado = read_file_content(test_file)
    assert esperado == resultado
