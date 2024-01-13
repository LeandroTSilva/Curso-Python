'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. 
Calcule e mostre o comprimento da hipotenusa.

'''

from math import hypot

valorCatetoOposto = float(input(' Digite o valor do cateto oposto \n'))
valorCatetoAdjacente = float(input(' Digite o valor do cateto adjacente \n'))

print(' *** ' * 20)
print(' O valor da hipotenusa é {:.2f}'.format(hypot(valorCatetoOposto, valorCatetoAdjacente)))



