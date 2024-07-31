"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução,
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

"""

fim = False
total = cont = media = maior = menor = 0
num = 0
while fim == False:
    num = int(input('Digite um numero: '))
    total += num
    cont += 1

    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num

    fim = input('Deseja continuar? [S/N] ').lower().strip()[0]
    if fim == 's':
        fim = False
    elif fim =='n':
        fim = True

media = total / cont

print('Você digitou {} numeros e a média foi {}.'.format(cont, media))
print('O menor numero digitado foi {} e o maior digitado foi {}'.format(menor, maior))
print('*** fim do programa ***')