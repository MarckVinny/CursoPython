
# #! Crie um algorítimo que leia um número e mostre o seu dobro,
# #! seu triplo e a raiz quadrada.

print('\n\
    \n:::::::::::::::::::::::::::::::::::::::\
    \n::: Veja o dobro, o triplo e a raiz :::\
    \n:::   quadrada do número digitado   :::\
    \n:::::::::::::::::::::::::::::::::::::::')

n1 = int(input('\nDigite um valor: '))
nd = n1 * 2
nt = n1 * 3
raiz = n1 ** (1/2)   # ou raiz = pow(n1, 1/2)

print('\
    \nVocê digitou: {}\
        \nSeu dobro é: {}\
            \nSeu triplo é: {}\
                \nE sua raiz quadrada é: {}'.format(n1, nd, nt, raiz))
