'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

'''

valorNumero = int(input('Digite um numero inteiro \n'))

tipoNumero = valorNumero % 2

if tipoNumero == 0:
    print('O número {} é Par'.format(valorNumero))
else:
    print('O número {} é Impar'.format(valorNumero))
