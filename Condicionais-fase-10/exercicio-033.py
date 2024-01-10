"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""
primeiroValor = int(input('Primeiro valor \n'))
segundoValor = int(input('Segundo valor \n'))
terceiroValor = int(input('Terceiro valor \n'))

maiorValor = max(primeiroValor, segundoValor, terceiroValor)
menorValor = min(primeiroValor, segundoValor, terceiroValor)

print('O maior numero digitado foi {}'.format(maiorValor))
print('O menor valor digitado foi {}'.format(menorValor))


