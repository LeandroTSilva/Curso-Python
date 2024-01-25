"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

"""


from random import randint

print('=-' * 20)
print(' Advinhe o numero que Estou Pensado ')
print('=-' * 20)

numeroComputador = randint(0, 10)

palpiteUsuario = int(input('Chute um numero de entre 0 e 10 \n'))
numeroTentativa = 0

while palpiteUsuario != numeroComputador:
    numeroTentativa += 1
    if palpiteUsuario > numeroComputador:
        palpiteUsuario = int((input('Menos... tente de novo \n')))
    elif palpiteUsuario < numeroComputador:
        palpiteUsuario = int(input('Mais... tente de novo \n'))

print('-=' * 20)
print('VENCEDOR! eu pensei em {} e você em digitou {}, foram {} tentativas ao todo'.format(numeroComputador, palpiteUsuario, numeroTentativa)) 

print(' **** Fim de Jogo **** ')