
# ? DESCOMENTE O BLOCO DE CÓDIGO COM CTRL+Ç E TESTE ###

# # todo: Alinha o 'nome' à esquerda (de 20 caracteres)
# # !     o alinhamento padrão é à esquerda {:20}.
#
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:20}!'.format(nome))

# # todo: Alinha o 'nome' à esquerda (de 20 caracteres)
# # todo: utilizando o sinal de menor '<'
# # todo: e preenche o restante do espaço com '='
#
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:=<20}!'.format(nome))

# # todo: Alinha o 'nome' à direita (de 20 caracteres)
# # todo: utilizando o sinal de maior '>'
# # todo: e preenche o restante do espaço com '='
#
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:=>20}!'.format(nome))

# # todo: Alinha o 'nome' ao centro (de 20 caracteres)
# # todo: utilizando o acento circunflexo '^'
# # todo: e preenche o restante do espaço com '='
#
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:=^20}!'.format(nome))

# # todo: Alinha o 'nome' ao centro (de 20 caracteres)
# # todo: utilizando o acento circunflexo '^'
#
# nome = input('Qual é seu nome? ')
# print('Prazer em te conhecer {:^20}!'.format(nome))

# ! REPLICANDO INFORMAÇÕES
# todo: Serão digitados pelo usuário 2 números que serão convertidos
# todo: em números inteiros, definir variáveis que conterão esses valores
# todo: digitados, e depois realizar os cálculos das variáveis.

print('\n\n::: Calculando e Replicando seus Valores :::\n')

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
r = n1 % n2
e = n1 ** n2

print('\nA soma é: {}\
        \nO produto é: {}\
            \nA divisão é: {:0.2f}\
                \nA divisão inteira é: {}\
                    \nO resto da divisão é: {}\
                        \nA potência é: {}'.format(s, m, d, di, r, e))
