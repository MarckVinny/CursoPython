
# #? Crie um programa que leia quanto dinheiro o usuário tem
# #? na carteira e mostre quantos dólares ela pode comprar.
# #! Obs.: considere o dólar à R$ 3,27

print('\n\
    \n::::::::::::::::::::::::::::::::\
    \n::::: Conversor Dólar/Real :::::\
    \n::::::::::::::::::::::::::::::::')

n1 = float(input('\nQuantos Reais você possui? '))
dolar = float(3.27)
conv = n1 / dolar

print('\
    \nVocê possui R$ {:.2f}\
        \nE pode comprar $ {:.2f} dólares.'.format(n1, conv))
