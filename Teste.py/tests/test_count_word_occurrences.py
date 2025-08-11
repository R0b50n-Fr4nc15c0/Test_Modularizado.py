from Functions.count_word_occurrences import count_word_occurrences

#---------contagem de palavras---------

def test_count_word():
    text = "Bom dia, boa tarde ou boa noite"
    word = "boa"
    esperado = 2
    resultado = count_word_occurrences(text, word)
    assert esperado == resultado

