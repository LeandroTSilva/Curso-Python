"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

"""

valorSalario = float(input('Digite seu salário (R$) \n'))

if valorSalario > 1250.00:
    novoSalario = valorSalario + ((valorSalario * 10) / 100)
    print('Seu novo salário será R${:.2f}'.format(novoSalario))
else:
    novoSalario = valorSalario + ((valorSalario * 15) / 100)
    print('Seu novo salário será R${:.2f}'.format(novoSalario))
print(' ****  Até mais, Bom trabalho ;) **** ')



