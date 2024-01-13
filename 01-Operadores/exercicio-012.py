'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

'''

valorProduto = float(input(' Digite o valor do produto \n'))
valorDesconto = float(input(' Digite o valor em % para aplicar o desconto \n'))

totalDesconto = valorProduto - (valorProduto * valorDesconto) / 100

print(' * ' * 40)
print('Valor do Produto R${:.2f}'.format(valorProduto))
print('Total a pagar com desconto de 5% é {:.2f}'.format(totalDesconto))
