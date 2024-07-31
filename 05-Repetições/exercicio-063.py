"""
Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

"""

num = int(input('Quantos termos deseja mostrar \n'))
termo1 = 0
termo2 = 1
cont = 3

print('{} -> {}'.format(termo1, termo2), end='')

while cont <= num:
    termo3 = termo1 + termo2
    print('-> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1

print('\n *** Fim do Programa *** \n')
