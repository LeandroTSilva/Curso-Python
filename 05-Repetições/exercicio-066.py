"""
Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

"""

num = cont = total = 0
while True:
    num = int(input('Digite um numero [999 para encerrar]: '))
    if num == 999:
        break
    total += num
    cont += 1

print(f'Você digitou {cont} numeros, e a soma entre eles é {total}')
