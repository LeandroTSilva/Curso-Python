'''
 Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

'''

numEntrada = int(input(' Digite um numero inteiro \n'))

numDobro = numEntrada * 2
numTriplo = numEntrada * 3
numRaiz = numEntrada ** (1/2)

print(' - ' * 40)

print(' O dobro de {} é {}, o triplo é {}, e sua raiz quadrada {}'.format(numEntrada, numDobro, numTriplo, numRaiz))