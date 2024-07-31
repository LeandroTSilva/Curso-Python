"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.

"""
print('-' * 12)
print('GERADOR DE P.A (PROGRESSÃO ARITIMÉTICA)')
print('-' * 12)


termo01 = int(input('Digite o valor do 1º termo \n'))
razao = int(input('Digite agora o valor da Razão \n'))
cont = 1
total = 0
maisTermo = 10

while maisTermo != 0:
     total = total + maisTermo
     while cont <= total:
          print('{} -> '.format(termo01), end='')
          termo01 += razao
          cont += 1
     print('Pausa')
     maisTermo = int(input('Quantos termos a mais deseja mostra? \n'))
     print('Foram exibidos {} termos no total'.format(total))

print('\n *** fim do programa ***')