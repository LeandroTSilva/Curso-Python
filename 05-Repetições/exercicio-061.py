"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

"""
print('-' * 12)
print('GERADOR DE P.A (PROGRESSÃO ARITIMÉTICA)')
print('-' * 12)


termo01 = int(input('Digite o valor do 1º termo \n'))
razao = int(input('Digite agora o valor da Razão \n'))
cont = 1

while cont <= 10:
     print('{} -> '.format(termo01), end='')
     termo01 += razao
     cont += 1


print('\n *** fim do programa ***')

