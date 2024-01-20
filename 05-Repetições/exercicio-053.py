"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

Este exercicio fiquei perdido e não souber como fazer até ver a correção, nem me dei conta de que podia usar manipulação de textos para resolver, 
pois pensei apenas em como fazer para "ler" a frase.



alternativa ensinada na correção:

em lugar da estrutura "for" usar as técnicas de fatiamento.

invertido = fraseJunto[: : -1]


"""

frase = str(input('Digite uma frase \n')).strip().lower()
fraseSeparada = frase.split()
fraseJunto = ''.join(fraseSeparada)

invertido = ''

for leitor in range(len(fraseJunto)-1, -1, -1):
    invertido += fraseJunto[leitor]
if fraseJunto == invertido:
    print('a frase é {} e invertida é {}, É UM PALÍNDROMO'.format(fraseJunto, invertido))
else:
    print(' a frase é {} e invertida fica {} NÃO É PALÍNDROMO'.format(fraseJunto,invertido))
