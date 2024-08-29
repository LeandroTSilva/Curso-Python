"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""
from random import randint
num = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5))

print('-' * 30)
print('{:^30}'.format('Sorteio com Tuplas'))
print('-' * 30)

print(f'Os numeros sorteados foram: ', end=' ')
for c in num:
    print(f'|{c}|', end=' ')
print(f'\n O maior valor sorteado foi: -> {max(num)}')
print(f' O menor valor sorteado foi: -> {min(num)}')

