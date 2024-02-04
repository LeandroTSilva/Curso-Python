"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120


Solução alternativa usando a bibliote match
valorFatorial = factorial(valorEntrada)
print(valorFatorial)

"""

valorEntrada = int(input('informe um numero inteiro positivo \n'))
valorFatorial = 1
cont = valorEntrada


print('-=' * 12)
print('{}! = '.format(valorEntrada),end=(''))

while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    valorFatorial *= cont
    cont -= 1

print('{}'.format(valorFatorial))
print('-=-=-=-= Fim do Programa -=-=-=-=')
