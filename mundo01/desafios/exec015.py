
# #? Escreva um programa que pergunte a quantidade de
# #? Km percorridos por um carro alugado e a quantidade de
# #? dias pelos quais foi alugado.
# #todo: Calcule o preço a pagar, sabendo que o carro custa
# #todo: R$ 60,00 por dia e R$ 0,15 por Km rodado.

import os

os.system('clear')  # Limpa o terminal antes de rodar o código

print('\
    \n:::::::::::::::::::::::::\
    \n:::    Programa de    :::\
    \n::: Aluguel de Carros :::\
    \n:::::::::::::::::::::::::')

nkm = float(input('\nQuantos Km foram percorridos? '))
"""Número de Km percorridos
    """
ndias = int(input('\nQuantos dias foi alugado? '))
"""Número de dias alugados
    """
aluguel = 60 * ndias
"""Cálculo do Aluguel

    Multiplica a o valor do aluguel pela quantidade de dias
    """
km = 0.15 * nkm
"""Cálculo do Km rodado

    Multiplica o valor do Km pelo Km rodado
    """
preco = aluguel + km

print(f'\
    \nForam percorridos {nkm:.2f} Km.\
        \nO carro foi alugado por {ndias} dias.\
            \nValor total a pagar: R$ {preco:.2f}')
