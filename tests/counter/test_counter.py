from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "Python"
    expected_count= 5
    result = count_ocurrences(path, word)
    assert result == expected_count, f"A contagem para a palavra '{word}' no arquivo '{path}' está incorreta. Esperado: {expected_count}, Obtido: {result}"