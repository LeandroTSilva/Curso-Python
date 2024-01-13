'''
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

'''



diasAlugado = float(input('Quantos dias uso o carro? \n'))
kmRodado = float(input('Quanto km rodado? \n'))

totalDia = diasAlugado * 60.00
totalKm = kmRodado * 0.15

print(' *** ' * 20)
print('Total a paga pelo carro é de R${:.2f}'.format((totalDia + totalKm)))


