"""
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

numExtenso = ('Zero','Um','Dois','Três','Quatro',
              'Cinco','Seis','Sete','Oito',
              'Nove','Dez','Onze','Doze',
              'Treze','Catorze','Quinze','Dezesseis'
              ,'Dezessete','Dezoito','Dezenove','Vinte')
while True:
    while True:
        numTeclado = int(input('Digite um numero inteiro entre 0 e 20 \n'))
        if numTeclado >= 0 and numTeclado <= 20:
            break
        print('Você digitou fora do intervalo, tente de novo', end=' ')

    print('-' * 30)
    print(f'{numTeclado} em extenso é: {numExtenso[numTeclado]} \n')
    resp = input('Deseja continuar? [S/N] \n').strip().lower()[0]
    if resp == 'n':
        break

print('Fim do programa')
