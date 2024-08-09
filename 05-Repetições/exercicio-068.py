"""
 Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
 mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""
from random import randint
vJogador = 0
vComputador = 0

while True:
    print('-' * 20)
    num = int(input('Digite um valor [entre 0 e 10]: '))
    tipo = (input('Par ou Impar [P/I]')).strip().lower()[0]

    computador = randint(0, 10)
    par = (num + computador) % 2

    if par == 0 and tipo == 'i':
        print('x' * 4 + ' VOCÊ PERDEU ' + 'x' * 4)
        print(f'Total: {num + computador} PAR! \nvocê jogou {num} e computador jogou {computador} \n')
        vComputador += 1
        break

    elif par != 0 and tipo == 'p':
        print('x' * 4 + ' VOCÊ PERDEU ' + 'x' * 4)
        print(f'Total: {num + computador} IMPAR! \nvocê jogou {num} e computador jogou {computador} \n')
        vComputador += 1
        break

    elif par != 0 and tipo == 'i':
        print('*' * 4 + ' VOCÊ VENCEU! ' + '*' * 4)
        print(f'Total: {num + computador} IMPAR! \nvocê jogou {num} e computador jogou {computador} \n')
        vJogador += 1

    elif par == 0 and tipo == 'p':
        print('*' * 4 + ' VOCÊ VENCEU! ' + '*' * 4)
        print(f'Total: {num + computador} PAR! \nvocê jogou {num} e computador jogou {computador} \n')
        vJogador += 1

print('>>>>>>>>>>>> PLACAR FINAL <<<<<<<<<<<< ')
print(f'     Jogador: {vJogador} x Computador: {vComputador}  ')
print('>>>>>>>>>>>> FIM DE JOGO! <<<<<<<<<<<< ')







