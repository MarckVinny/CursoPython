print ('====== Desafio 04 =====')
# Crie um programa que leia algo digitado no teclado e mostre na Tela 
# o seu Tipo Primitivo e todas as informações possíveis sobre ela.

n = input('Digite algo: ')

print ('\nO Tipo Primitivo desde valor é: {} \
    \nSó tem espaços? {} \
        \nÉ um número? {} \
            \nE alfabético? {} \
                \nÉ alfanumérico? {} \
                    \nEstá em maiúsculas? {} \
                        \nEstá em minúsculas? {} \
                            \nEstá capitalizada? {}'.format(type(n), 
                                                        n.isspace(), 
                                                        n.isnumeric(), 
                                                        n.isalpha(), 
                                                        n.isalnum(), 
                                                        n.isupper(), 
                                                        n.islower(), 
                                                        n.istitle()
                                                        ))

