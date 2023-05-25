def is_palindrome_recursive(word, low_index, high_index):
    """Faça o código aqui."""
    if low_index >= high_index:
        return True
    # Retorne True se a palavra passada por parâmetro for um palíndromo;

    if word[low_index] != word[high_index]:
        return False
    # Retorne False se a palavra passada por parâmetro não for um palíndromo;

    if len(word) == 0:
        return False
    #  Retorne False se nenhuma palavra for passada por parâmetro

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    #  verifica uma subpalavra da palavra original,
    #  exclui a primeira e a ultima letra
