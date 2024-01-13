'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

'''

valorReal = float(input(' Digite quanto você tem em (R$) \n'))

taxaCambio = float(input(' Digite a taxa de cambio atual em dolar (U$). \n'))

valorDolar = valorReal * taxaCambio

print(' - ' * 40)

print(' Com R${:.2f} você pode comprar U${:.2f} em dolar'. format(valorReal, valorDolar))

