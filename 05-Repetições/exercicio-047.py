"""
 Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

"""


# recomendado: for c in range(2, 51, 2), pois reduz o numero de laços/iterações executados no programa

for c in range(1, 51, 1):
    if c % 2 == 0:
        print(c, end=' ')
print(' >>> Fim dos pares <<< ')
