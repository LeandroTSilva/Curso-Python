"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa

"""
from time import sleep


fimPrograma = False

valorEntrada = int(input('Digite um numero inteiro \n'))
valorEntrada2 = int(input('Digite outro numero inteiro \n'))

while fimPrograma == False:
    menuUsuario = int(input("""
Suas Opções:
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Numeros
    [5] - Sair do Programa
"""))
    

    if menuUsuario == 1:
        print('Opção escolhida: Soma')
        total = valorEntrada + valorEntrada2
        print('A Soma entre {} + {} é {} '.format(valorEntrada, valorEntrada2, total))

    elif menuUsuario == 2:
        print('Opção escolhida: Multiplicar')
        produto = valorEntrada * valorEntrada2
        print('{} x {} é igual a {} '.format(valorEntrada, valorEntrada2, produto))

    elif menuUsuario == 3:
        print('Opção escolhida: Maior')
        if valorEntrada > valorEntrada2:
            print('{} é maior que {}'.format(valorEntrada, valorEntrada2))
        elif valorEntrada == valorEntrada2:
            print('{} é igual a {}'.format(valorEntrada,valorEntrada2))
        else:
            print('{} é maior que {}'.format(valorEntrada2,valorEntrada))

    elif menuUsuario == 4:
        print('Opção escolhida: Novos numeros')
        valorEntrada = int(input('Insira um novo numero inteiro \n'))
        valorEntrada2 = int(input('Insira um outro numero inteiro \n'))

    elif menuUsuario == 5:
        print('Saindo....')
        sleep(1.8)
        fimPrograma = True

    else:
        print('Entrada inválida, tente de novo!')

print(' >>>> Fim do Programa <<<< ')
