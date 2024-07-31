"""
 Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


"""
# Segue meu código Original

'''
Trecho com minha solução antes da correção |GAMBIARRA TOTAL

parar = False
soma = 0
cont = 0
while parar == False:
    num = int(input('Digite um numero [999 para encerrar]: '))
    soma += num
    cont += 1
    if num == 999:
        parar = True
    else:
        para = False
print('Você digitou {} numeros, e a soma entre eles é {}'.format(cont - 1, soma - 999))

'''

## solução provisória do Guanabara (é gambiarra mas só até a aula 15) playlist python mundo 2

num = cont = soma = 0
num = int(input('Digite um numero [999 para encerrar]: '))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um numero [999 para encerrar]: '))
print('Você digitou {} números e a soma entre ele é: {}'.format(cont, soma))
