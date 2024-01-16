"""
Tabuada 2.0
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

"""

valorEntrada = int(input('Digite um numero para mostrar a tabuada \n'))

valorOperacao = int(input("""
Escolha a operação:

    [1] - Adição
    [2] - Subtração
    [3] - Multiplicação
    [4] - Divisão (Exata)
    [5] - Divisão (com precisão decimal)
"""))


# Adição
if valorOperacao == 1:
    print('Operação escolhida: Adição')
    print('Operação escolhida: {}'.format(valorOperacao))
    for c in range(0, 11):
        parcela = valorEntrada + c
        print('{} + {} = {}'.format(valorEntrada, c, parcela))




# Subtração
elif valorOperacao == 2:
    print('Operação escolhida: Subtração')
    for c in range(0, 11):
        resto = valorEntrada - c
        print('{} - {} = {}'.format(valorEntrada, c, resto))




# Multiplicação
elif valorOperacao == 3:
    print('Operação escolhida: Multiplicação')
    for c in range(0, 11):
        produto = valorEntrada * c
        print('{} x {} = {}'.format(valorEntrada, c, produto))



# Divisão Exata
elif valorOperacao == 4:
    print('Operação escolhida: Divisão exata')
    if valorEntrada == 0:
        print('Impossível dividir por Zero (0)')
    else:
        for c in range(1, 11):
            divisaoExata = valorEntrada // c
            print('{} : {} = {}'.format(valorEntrada, c, divisaoExata))



# Divisão Decimal

elif valorOperacao == 5:
    print('Operação escolhida: Divisão c/ Precisão decimal')
    if valorEntrada == 0:
        print('Impossível dividir por Zero(0)')
    else:
        for c in range(1, 11):
            divisaoDecimal = valorEntrada / c
            print('{} : {} = {:.2f}'.format(valorEntrada, c, divisaoDecimal))


else:
    print('Entrada Inválida, tente de novo')











