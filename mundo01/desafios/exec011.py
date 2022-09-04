
# #? Faça um programa que leia a largura e a altura de uma parede em metros,
# #? calcule a sua área e a quantidade de tinta necessária para pintá-la,
# #? sabendo que a cada litro de tinta pinta uma área de 2m quadrado.

print('\n\
    \n:::::::::::::::::::::::::::::\
    \n::::: Cálculo de Área e :::::\
    \n:::: Rendimento de Tinta ::::\
    \n:::::::::::::::::::::::::::::')

larg = float(input('\nQual a largura da Parede em metros? '))
"""Define a largura da Parede em metros
    """
altura = float(input('Qual é a Altura da Parede em metros? '))
"""Define a Altura da Parede em metros
    """
area = larg * altura
"""Calcula a área da parece
    """
rend = area / 2

print('\
    \nLargura: {:.2f} m\
        \nAltura: {:.2f} m\
            \nÁrea: {:.2f} m\u00b2\
                \nVocê precisará de {:.2f} litros de tinta.'
      .format(larg, altura, area, rend))
