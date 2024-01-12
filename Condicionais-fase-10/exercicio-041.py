"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER

"""
print('=-=' * 20)
print(' *** Curso Em Vídeo Natação *** ')
print('=-=' * 20)

from datetime import date

anoNascimento = int(input('Ano de nascimento? \n'))
anoAtual = date.today().year

idadeAtleta = anoAtual - anoNascimento

if idadeAtleta <= 9:
    print('O atleta tem {} anos, sua categoria é: MIRIM'.format(idadeAtleta))
elif idadeAtleta > 9 and idadeAtleta <= 14:
    print('O atleta tem {} anos, sua categoria é: INFANTIL'.format(idadeAtleta))
elif idadeAtleta > 14 and idadeAtleta <= 19:
    print('O atleta tem {} anos, sua categoria é: JUNIOR'.format(idadeAtleta))
elif idadeAtleta > 19 and idadeAtleta <= 25:
    print('O atleta tem {} anos, sua categori é: SÊNIOR'.format(idadeAtleta))
elif idadeAtleta > 25:
    print('O atleta tem {} anos: sua categoria é: MASTER'.format(idadeAtleta))
