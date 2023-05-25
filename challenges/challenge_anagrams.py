def class_string(letters):
    if len(letters) <= 1:
        return letters
        # Verifica se a lista de letras tem tamanho menor ou igual a 1.
    menor_sup = [abcd for abcd in letters[1:] if abcd < letters[0]]
    # cria uma lista com as letras menores que o suporter
    maior_sup = [abcd for abcd in letters[1:] if abcd >= letters[0]]
    # cria uma lista com as letras maiores ou iguais ao suporte
    return class_string(menor_sup) + [letters[0]] + class_string(maior_sup)
    # retorna a função e combina as listas na ordem correta
    # letters[1:] neste trexo esta basicamente "fatiando" a string
    # do inicio dela, sem contar o 1
    # https://docs.python.org/pt-br/3/tutorial/introduction.html#lists


def is_anagram(first_string, second_string):
    first_string = "".join(class_string(list(first_string.lower())))
    second_string = "".join(class_string(list(second_string.lower())))
    # transforma as strings em uma lista de letras minúsculas e chama a
    # função sort_string para organizar.
    # Retorne True se as palavras passadas forem anagramas
    # sem diferenciar maiúsculas e minúsculas.

    if not first_string or not second_string:
        # Retorne False se alguma das palavras passadas por
        # parâmetro for uma string vazia

        return (first_string, second_string, False)
        # Retorne False se as palavras passadas por parâmetro não
        # forem anagramas

    return (first_string, second_string, first_string == second_string)
    # Retorne True se as palavras passadas por parâmetro forem anagramas;
