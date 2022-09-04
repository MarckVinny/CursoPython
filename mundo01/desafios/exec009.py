
# #? Faça um programa que leia um número inteiro
# #? qualquer e mostre a sua tabuada.

print('\n\
    \n::::::::::::::::::::::::::::::::\
    \n:::::: Gerador de Tabuada ::::::\
    \n::::::::::::::::::::::::::::::::')

n1 = int(input('\nDigite um número e Gere sua Tabuada de Multiplicação: '))

print('\
    \n::::::::::::::::::::\
    \n:: Tabuada de{: ^5}::\
    \n::::::::::::::::::::\
    \n:{: >5} x 1 = {: <5} :\
    \n:{: >5} x 2 = {: <5} :\
    \n:{: >5} x 3 = {: <5} :\
    \n:{: >5} x 4 = {: <5} :\
    \n:{: >5} x 5 = {: <5} :\
    \n:{: >5} x 6 = {: <5} :\
    \n:{: >5} x 7 = {: <5} :\
    \n:{: >5} x 8 = {: <5} :\
    \n:{: >5} x 9 = {: <5} :\
    \n:{: >5} x 10 = {: <5}:\
    \n::::::::::::::::::::\
        '.format(n1, n1, (n1 * 1),
                 n1, (n1 * 2),
                 n1, (n1 * 3),
                 n1, (n1 * 4),
                 n1, (n1 * 5),
                 n1, (n1 * 6),
                 n1, (n1 * 7),
                 n1, (n1 * 8),
                 n1, (n1 * 9),
                 n1, (n1 * 10)))
