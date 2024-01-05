'''
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.


'''

salarioAtual = float(input(' Digite seu salario atual (R$) \n'))
valorAjuste = salarioAtual + (salarioAtual * 15) / 100

print(' * ' * 40)
print( 'Seu salario com 15% de aumento será de R${:.2f}'.format(valorAjuste))

