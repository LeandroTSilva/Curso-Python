"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais

"""
print('=-=' * 20)
print(' *** Comparador de numeros *** ')
print('=-=' * 20)

valor1 = int(input('Digite o primerio numero \n'))
valor2 = int(input('Digite o segundo numero \n'))

if valor1 > valor2:
    print('O numero {} é MAIOR que numero {}'.format(valor1,valor2))
elif valor2 > valor1:
    print('O numero {} é MAIOR que numero {}'.format(valor2, valor1))
elif valor1 == valor2:
    print('Os numeros {} e {} são IGUAIS'.format(valor1, valor2))
else:
    print('Entrada invalida, tente de novo')
    