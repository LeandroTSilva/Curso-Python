"""
Calculadora de tabuada

Programa que lê um numero inteiro, sem seguida o usuário escolhe a operação e mostra a respectiva tabuada


"""

print('-=' * 6 + '  TABUADA 2.0 EXTRA  ' + '-=' * 6)

fimPrograma =False
cont = 0

while fimPrograma == False:
    num = int(input('Digite um numero para mostrar a tabuada \n'))
    operacao = int(input("""
    
    Escolha a Operação:
    [ 1 ] - Soma
    [ 2 ] - Subtração
    [ 3 ] - Multiplicação
    [ 4 ] - Divisão     
    
    """))

    if operacao == 1:
        while cont <= 20:
            total = num + cont
            print('{:2} + {:2} = {:2}'.format(num, cont, total))
            cont += 1
        fimPrograma = input('Deseja fazer outro cálculo: (S) - Sim | (N) - Não \n').lower()
        if fimPrograma == 's':
            fimPrograma = False
            cont = 0
        elif fimPrograma == 'n':
            fimPrograma = True
        else:
            print('Entrada Inválida')

    if operacao == 2:
        while cont <= 20:
            sub = num - cont
            print('{:2} - {:2} = {:2}'.format(num, cont, sub))
            cont += 1
        fimPrograma = input('Deseja fazer outro cálculo: (S) - Sim | (N) - Não \n').lower()
        if fimPrograma == 's':
            fimPrograma = False
            cont = 0
        elif fimPrograma == 'n':
            fimPrograma = True
        else:
            print('Entrada Inválida')

    if operacao == 3:
        while cont <= 10:
            produto = num * cont
            print('{:2} x {:2} = {:2}'.format(num, cont, produto))
            cont += 1
        fimPrograma = input('\n Deseja fazer outro cálculo: (S) - Sim | (N) - Não \n').lower()
        if fimPrograma == 's':
            fimPrograma = False
            cont = 0
        elif fimPrograma == 'n':
            fimPrograma = True
        else:
            print('Entrada Inválida')

    if operacao == 4:
        if num == 0:
            print('OOPS!!! Você digitou {:2}, Não existe divisão por 0 (Zero)'.format(num))
            fimPrograma = input('Deseja continuar, mas com outro numero? (S) - Sim | (N) - Não \n ').lower()
            if fimPrograma == 's':
                fimPrograma = False
                cont = 0
            elif fimPrograma == 'n':
                fimPrograma = True
        elif num != 0:
            cont = 1
            while cont <= 10:
                divisao = num / cont
                print('{:2} / {:2} = {:2.2f}'.format(num, cont, divisao))
                cont += 1
            fimPrograma = input('Deseja fazer outro cálculo? (S) - Sim | (N) - Não \n').lower()
            if fimPrograma == 's':
                fimPrograma = False
                cont = 0
            elif fimPrograma == 'n':
                fimPrograma = True
            else:
                print('Entrada inválida')




print('Fim do programa')