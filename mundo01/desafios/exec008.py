
# #? Escreva um programa que leia valor em metros e o exiba
# #? convertido em centímetros e milímetros.

print('\n\
    \n::::::::::::::::::::::::::::::::\
    \n::: Conversor de Metros para :::\
    \n::: Centímetros e Milímetros :::\
    \n::::::::::::::::::::::::::::::::')

n1 = float(input('\nDigite uma medida em Metros: '))
cm = n1 * 100
mm = n1 * 1000

print('\
    \n{} metros equivale à: {} centímetros\
        \n{} metros é o mesmo que: {} milímetros'.format(n1, cm, n1, mm))
