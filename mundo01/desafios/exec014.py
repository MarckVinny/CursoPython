
# #? Escreva um programa que converta a temperatura
# #? digitada em ºC e a converta para ºF.
# #todo: A fórmula para a conversão de
# #todo: ºC para ºF é: ((9 * ºC) / 5) + 32

import os

os.system('clear')  # Limpa o terminal antes de rodar o código

c = float(input('\n\nIndorme a temperatura em ºC: '))
f = ((9 * c) / 5) + 32

print(f'\nA temperatura de {c} ºC corresponde a {f} ºF')
