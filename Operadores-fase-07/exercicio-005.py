'''
Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

'''

numeroFornecido = int(input(' Digite um numero inteiro qualquer \n'))

numAntecessor = numeroFornecido - 1
numSucessor = numeroFornecido + 1

print(' - ' * 40 )

print(' Analisando o {} seu antecessor é {} e o seu sucessor é {}'.format(numeroFornecido, numAntecessor, numSucessor))

