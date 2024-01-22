"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""


maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
    pesoPessoa= float(input('Digite o peso da {}ª pessoal \n'.format(c)))
    if c == 1:
        maiorPeso = pesoPessoa
        menorPeso = pesoPessoa
    elif pesoPessoa > maiorPeso:
        maiorPeso = pesoPessoa
    elif pesoPessoa < menorPeso:
        menorPeso = pesoPessoa


print('O menor peso digitado foi: {:.2f}'.format(menorPeso))
print('O maior peso digitado foi: {:.2f}'.format(maiorPeso))
