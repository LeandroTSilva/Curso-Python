"""
Crie um programa que faça o computador jogar Jokenpô com você.

Neste exercício eu consegui densenvolver corretamente a lógica das condicionais aninhadas, Porém me atrapalhei na hora de randomizar e 
exbir Pedra, Papel e Tesoura tanto para jogador quanto para computador.

revisar alguns modulos na documentação pode me ajudar na próxima

"""


from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
jogador = int(input('''
Suas opções:
    [0] Pedra
    [1] Papel
    [2] Tesoura
                    
Qual a sua jogada?
'''))


print('Computador jogou {}'.format(itens[computador]))
print('O Jogador jogou {}'.format(itens[jogador]))



# jogou Pedra

if computador == 0: 
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador Vence !!')
    elif jogador == 2:
        print('Computador Vence !!')
    else:
        print('Entrada Inválida, tente de novo')

# jogou Papel

elif computador == 1: 
    if jogador == 1:
        print('Empate')
    elif jogador == 0:
        print('Computador Vence !!')
    elif jogador == 2:
        print('Jogador Vence !!')
    else:
        print('Entrada Inválida, tente de novo')

# jogou Tesoura 

elif computador == 2: 
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('Jogador Vence !!')
    elif jogador == 1:
        print('Computador Vence !!')
    else:
        print('Entraa Inválida, tende de novo')
else:
    print(' *** Fim de Jogo ***')