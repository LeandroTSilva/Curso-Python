"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

"""

from datetime import date

print('=-=' * 20)
print(' *** Forças Armadas Brasileiras *** ')
print('=-=' * 20)

anoAtual = date.today().year
anoNascimento = int(input('Ano de nascimento? \n'))

idadeAtual = anoAtual - anoNascimento
idadeAlistamento = 18 - idadeAtual


if idadeAtual < 18 :
    print('Você tem {} anos, Faltam {} anos para se alistar, e deverar se alsitar em {}'.format(idadeAtual,idadeAlistamento, anoAtual + idadeAlistamento))
elif idadeAtual == 18:
    print('Em {} você completa {} anos, ALISTE-SE IMEDIATAMENTE'. format(anoAtual, idadeAtual))
elif idadeAtual > 18:
    idadeAlistamento = idadeAtual - 18
    print('Você tem {} anos, ja se apresentou há {} anos, no ano de {}'.format(idadeAtual, idadeAlistamento, anoAtual - idadeAlistamento))
    print('*** caso não tenha de apresentado em {}, SE APRESENTE URGENTE'. format(anoAtual - idadeAlistamento))
else:
    print('Entrada inválida tente de novo')





