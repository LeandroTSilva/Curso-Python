'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.

'''

velocidadeCarro = float(input('Qual a velocidade atual do carro? (Km/h) \n'))

if velocidadeCarro <= 80.00:
    print('=-' * 20)
    print('Tenha um bom dia, Dirija com segurança!')
else:
    valorMulta = (velocidadeCarro - 80.00) * 7.00
    print('XXX' * 20)
    print('MULTADO! você excedeu o limite de velocidade que é 80km/h, sua multa será de:R${:.2f}'.format(valorMulta))
