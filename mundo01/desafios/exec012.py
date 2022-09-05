
# #? Faça um algorítimo que leia o preço de um produto
# #? e mostre seu novo preço com 5% de desconto.

print('\n\
    \n:::::::::::::::::::::::::::::::\
    \n::::: Produto com Desconto ::::\
    \n:::::::::::::::::::::::::::::::')

vprod = float(input('\nQual o valor do produto? '))
"""Define o valor do produto
    """
desc = vprod - (vprod * 5 / 100)
"""Define o desconto do produto
    """
print('\
    \nO valor do produto é R$ {:.2f}\
        \nValor com Desconto R$ {:.2f}\
            \n\nBoas compras e Volte Sempre!'.format(vprod, desc))
