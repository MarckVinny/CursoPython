# :::: Exercício Aula 04 :::
# Como deveria ter sido feito

# n1 = input('Digite um número: ')
# n2 = input('Digite outro: ')
# s = n1 + n2

# print('A soma vale: ', s)

#############################

# Forma correta

print(':::: Exercício Aula 04 - Desafio 03 ::::')
print('')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1 + n2

# Forma Obsoleta
# print('A soma entre ', n1, 'e', n2, 'vale: ', s)

print('A soma entre {} e {} vale: {}'.format(n1, n2, s))
