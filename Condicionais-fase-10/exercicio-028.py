'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.

'''



from random import randint

print('=-' * 20)
print(' Advinhe o numero que Estou Pensado ')
print('=-' * 20)

numeroComputador = randint(0, 6)

palpiteUsuario = int(input('Chute um numero de entre 0 e 5 \n'))

if palpiteUsuario == numeroComputador:
    print(' Parabéns eu pensei em {}, e você acertou ao chutar {}'.format(numeroComputador, palpiteUsuario))
else:
    print('Infelizmente você errou, eu pensei {} e você chutou {}'.format(numeroComputador, palpiteUsuario))
print(' **** Fim de Jogo **** ')
