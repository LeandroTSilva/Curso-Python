"""
 Desenvolva um programa que leia o comprimento de três segmentos e diga ao usuário se elas podem ou não formar um triângulo.

"""

segmento1 = float(input('Digite o segmento 1 \n'))
segmento2 = float(input('Digite o segmento 2 \n'))
segmento3 = float(input('Digite o segmento 3 \n'))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('Com os valores {}, {} e {} é possível obter um triângulo'.format(segmento1, segmento2, segmento3))
else:
    print('Com os valores {}, {} e {} NÃO é possível obter um triângulo'.format(segmento1, segmento2, segmento3))
print(' **** Fim do Programa **** ')
