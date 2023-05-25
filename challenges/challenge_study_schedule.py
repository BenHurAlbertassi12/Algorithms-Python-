def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if type(target_time) != int:
        return None
    # Caso o target_time passado seja nulo, o valor retornado pela
    # função deve ser None (considere o horário 0 como um horário válido);
    count_people = 0
    # variavel par definir o numero de pessoa estudando
    for first_period, final_period in permanence_period:
        if type(first_period) != int or type(final_period) != int:
            return None
    # este 'for' seve para definir se algum dos numeros não é inteiro,
    # caso aconteça isso vai retornar como none
        if target_time in range(final_period, first_period - 1, -1):
            # começa contando de traz para frente
            # esse 'if' ve se o target_time está dentro do intervalo entre os
            # periudos, o rangeé usada para gerar uma sequência de números
            # entre final_period e first_period - 1.
            # Se target_time estiver nesse intervalo,
            # isso significa que uma pessoa está estudando durante esse tempo,
            # então incrementa count_people em 1.
            count_people += 1
    return count_people
