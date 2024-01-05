'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''
from math import trunc

valorEntrada = float(input(' Digite um numero real qualquer \n'))

print(' *** ' * 20)
print(' A porção de inteira de {} é {}'.format(valorEntrada, trunc(valorEntrada)))



