"""
exercício extra tabuada com estrutura While

"""

valorEntrada = int(input('Informe um número para mostrar sua tabuada \n'))
cont = 0

while cont <=10:
    produto = valorEntrada * cont
    print('{} x {} = {}'.format(valorEntrada, cont, produto))
    cont += 1

print('*** fim do Progrma ***')