"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

"""

distanciaViagem = float(input(' Qual a distância da viagem (Km) \n'))

if distanciaViagem <= 200.00:
    valorPassagem = distanciaViagem * 0.50
    print('Você vai fazer uma viagem de {:.0f}Km'.format(distanciaViagem))
    print('O valor da passagem será: R${:.2f}'.format(valorPassagem))
else:
    valorPassagem = distanciaViagem * 0.45
    print('Você vai fazer uma viagem de {:.0f}Km'.format(distanciaViagem))
    print('O valor da passagem será: R${:.2F}'.format(valorPassagem))

print(' **** BOA VIAGEM :) **** ')

