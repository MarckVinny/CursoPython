
# #? Desenvolva um programa que leia as duas notas de um aluno,
# #? calcule e mostre sua média.
# #todo: Obs.: se ñ estiver dando o resultado correto,
# #todo: prestar atenção na ordem de precedência.

print('\n\
    \n:::::::::::::::::::::::::::::\
    \n::: Veja a Média do Aluno :::\
    \n::: digitando suas Notas  :::\
    \n:::::::::::::::::::::::::::::')

n1 = float(input('\nDigite uma Nota: '))
n2 = float(input('Digite a outra Nota: '))
s = n1 + n2
media = s / 2

print('\
    \nNota 1: {}\
        \nNota 2: {}\
            \nmédia: {}'.format(n1, n2, media))
