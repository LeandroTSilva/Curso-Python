'''
 Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.


 Este execicio eu não consegui fazer sem ver as aulas de exercício 23
 pois, tentei fazer apenas com os métodos da aula 09 e esbarrei justamente de só aceitar entrada com milhar.

 o que segue é o código corrido pelo Profº Gustavo Guanabara


'''

numeroFornecido = int(input('Digite um numero inteiro entre 0 a 9999 \n'))

valorUnidade = numeroFornecido // 1 % 10
valorDezena = numeroFornecido // 10 % 10
valorCentena = numeroFornecido // 100 % 10
valorMilhar = numeroFornecido // 1000 % 10

print('*** Analisando o numero **** ')
print('A unidade é {}'.format(valorUnidade))
print('A dezena é {}'.format(valorDezena))
print('A centena é {}'.format(valorCentena))
print('E o milhar é {}'.format(valorMilhar))




