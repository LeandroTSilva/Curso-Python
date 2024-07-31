"""
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

 *** Versão com For ***
"""

while True:
    print('- ' * 30)
    num = int(input('Qual quer ver a tabuada \n'))
    print('- ' * 30)
    if num < 0:
        break
    for cont in range(0, 11):
        produto = num * cont
        print(f'{num} x {cont:2} = {produto:2}')

print('Acabou')