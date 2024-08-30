"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

# Tupla onde cada elemento recebe um numero inteiro pelo teclado
num = (
   int(input('Digite um numero inteiro: ')),
   int(input('Digite o segundo numero: ')),
   int(input('Digite o terceiro numero: ')),
   int(input('Digite o último numero: '))
        )

# valida se 9 foi digitado ou não
if 9 in num:
    print(f'\n O numero 9 apareceu {num.count(9)} vezes')
else:
    print('O numero 9 não foi digitado')

# valida se o numero 3 foi digitado e então mostra sua posição
if 3 in num:
    print(f' O numero 3 apareceu {num.index(3)+1}ª posição')
else:
   print('O valor 3 não foi digitado')

# verfica se os numeros digitados são pares, e quais são      
print(' Numeros pares: ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
print('')