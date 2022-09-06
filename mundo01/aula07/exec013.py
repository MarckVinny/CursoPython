
# #? Faça um algorítimo que leia o salário de um Funcionário
# #? e mostre seu novo salário com 15% de aumento.

print('\n\
    \n:::::::::::::::::::::::::::::\
    \n::::: Aumento de Salário ::::\
    \n:::::::::::::::::::::::::::::')

salario = float(input('\nQual o valor do salário? '))
"""Define o valor do salário
    """
aumento = salario + (salario * 15 / 100)
"""Define o aumento do salário
    """
print('\
    \nO valor do salário é R$ {:.2f}\
        \nNovo valor com Aumento R$ {:.2f}'.format(salario, aumento))
