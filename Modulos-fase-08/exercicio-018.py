'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

'''
from math import sin, cos, tan, radians

valorAngulo = radians(float(input(' Digite o angulo que você deseja \n')))


print(' *** ' * 20)
print(' O ângulo de {}, tem o cosseno de: {:.2f}'.format(valorAngulo, cos(valorAngulo)))
print(' O ângulo de {}, tem o seno de: {:.2f}'.format(valorAngulo, sin(valorAngulo)))
print(' O ângulo de {}, tem a tangente de: {:.2f}'.format(valorAngulo, tan(valorAngulo)))

