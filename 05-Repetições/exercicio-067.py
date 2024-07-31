"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""
cont = 0
while True:
    num = int(input('Qual tabuada quer ver? '))
    if num < 0:
        break
    while cont <= 10:
        produto = num * cont
        print(f'{num} x {cont:2} = {produto:2}')
        cont += 1
    cont = 0
print('acabou')

