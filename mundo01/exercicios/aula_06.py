## converte o numero que foi digitado em um float
#
# n = float(input('Digite um número: '))
# print(n, type(n))

# # Colocar ou não str significa a mesma coisa, 
# # pois estará convertendo uma string para uma string
#
# n = str(input('Digite algo: '))
# print(n, type(n))

# # bool, verifica verdadeiro ou falso 
# # Verdadeiro, caso algo tenha sido digitado 
# # Falso, quando não tiver sido digitado nada. Ex.: digitando tecla Enter
# #
# n = bool(input('Digite algo: '))
# print('\nFoi digitado algo? \n{} \n\nA variável é do Tipo  \n{}'.format(n, type(n)))

# # isnumeric() verifica se é possível converter o que foi digitado em um número
# # com o Tipo Primitivo int() antes do input()
# # 
# n = input('Digite algo: ')
# print('\nFoi digitado: {} \nÉ Numérico? \n{} \n\nA variável é do Tipo  \n{}'.format(n, n.isnumeric(), type(n)))

# # isalpha() verifica se o que foi digitado é Alfabético
# # 
# n = input('Digite algo: ')
# print('\nFoi digitado: {} \nÉ Alfabético? \n{} \n\nA variável é do Tipo  \n{}'.format(n, n.isalpha(), type(n)))

# # isalnun() verifica se o que foi digitado é Alfanumérico
# # 
# n = input('Digite algo: ')
# print('\nFoi digitado: {} \nÉ Alfanumérico? \n{} \n\nA variável é do Tipo  \n{}'.format(n, n.isalnum(), type(n)))

# isupper() verifica se o que foi digitado está tudo em maiúsculo
# 
n = input('Digite algo: ')
print('\nFoi digitado: {} \nEstá tudo em Maiúsculo? \n{} \n\nA variável é do Tipo  \n{}'.format(n, n.isupper(), type(n)))