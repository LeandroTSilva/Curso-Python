"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 
1 para binário, 2 para octal e 3 para hexadecimal.

"""
print('=-=' * 20)
print(' *** Conversor Bases Numéricas *** ')
print('=-=' * 20)

numeroEntrada = int(input('Digite um numero inteiro \n'))

baseEscolhida = int(input('Escolha [1] = Binário, [2] = Octal ou [3] = Hexadecimal para fazer a conversão \n'))

if baseEscolhida == 1:
    print('O numero {} em Binário é igual a: {}'.format(numeroEntrada, bin(numeroEntrada)[2:]))
elif baseEscolhida == 2:
    print('O numero {} em Octal é igual a {}'.format(numeroEntrada, oct(numeroEntrada)[2:]))
elif baseEscolhida == 3:
    print('O numero {} em Hexadecimal é igual a {}'.format(numeroEntrada, hex(numeroEntrada)[2:]))
else:
    print('Entrada invalida para numero ou alternativas, Digite novamente \n')

print('*** Fim do Programa ***')