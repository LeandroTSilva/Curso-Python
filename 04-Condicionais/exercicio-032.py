"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

anoEntrada = int(input('Digite o ano para saber se é bissexto ou não \n'))

anoBissexto = anoEntrada % 4

if anoBissexto == 0:
    print('O ano de {} é Bissexto'.format(anoEntrada))
else:
    print('O ano de {} Não é bissexto'.format(anoEntrada))



