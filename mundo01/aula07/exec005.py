
# #! Crie um programa que leia um número inteiro e mostre na tela
# #! o seu sucessor e seu antecessor.

print('\n\
    \n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::\
    \n::: Veja o antecessor e o sucessor do número digitado :::\
    \n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::')

n1 = int(input('\nDigite um valor: '))
na = n1 - 1
ns = n1 + 1

print('\
    \nO antecessor é: {}\
        \nVocê digitou: {}\
            \nO sucessor é: {}'.format(na, n1, ns))
