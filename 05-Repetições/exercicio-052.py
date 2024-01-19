"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

Este exercicio novamente me enrolei, devido aos conceitos matematicos, me atrapalhei na fórmula de cálculo e no laço for.

"""


numEntrada = int(input('Digite um numero \n'))
cont = 0

for c in range(1, numEntrada + 1):
    if numEntrada % c == 0:
      print('\033[33m', end=(' '))
      cont += 1
    else:
      print('\033[31m', end=(' '))
    print('{}'.format(c), end=' ')

print('\n\33[mO numero {} foi divisível {} vezes'.format(numEntrada, cont))

if cont == 2:
   print('Este numero é PRIMO')
else:
   print('Este numero não é PRIMO')