"""
 Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""

from datetime import date
anoAtual = date.today().year

maiorIdade = 0
menorIdade = 0

for c in range(1, 8):
    anoNascimento = int(input('Ano de nascimento da {}ª pessoa \n'.format(c)))
    idade = anoAtual - anoNascimento
    if idade >= 18:
        maiorIdade += 1
    else:
        menorIdade += 1
print('{} Pessoas são Maiores e {} pessoas são Menores'.format(maiorIdade, menorIdade))
