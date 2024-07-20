'''
 Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

'''


_valorPrimeiroTermo = int(input('Digite o valor para o 1º da PA: '))
_valorRazao = int(input('Digite agora o valor para Razão PA: '))
_valorTermo = _valorPrimeiroTermo
_cont = 1

while _cont <= 10:
    print('{} -> '.format(_valorTermo), end='')
    _valorTermo += _valorRazao
    _cont += 1


print('\n =====  Fim do Programa  ===== ')