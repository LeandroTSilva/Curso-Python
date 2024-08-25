"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato. 

"""

somaMaiorMil = cont = menorPreco = totalemCompras = 0
maisBarato = ''
resp = ''

while True:
    nomeProduto = input('Cadastre o nome do produto \n')
    precoProduto = float(input('Qual o preço do produto \n'))
    cont += 1

    totalemCompras = totalemCompras + precoProduto

    if precoProduto > 1000:
        somaMaiorMil +=1
        
    if cont == 1 or precoProduto < menorPreco:
        menorPreco = precoProduto
        maisBarato = nomeProduto
    

    resp = input('Deseja cadastrar mais produtos? [S/N]').strip().lower()[0]
    if resp == 'n':
        break

print('\n--------------------------------------')
print(f'Total em compras: R${totalemCompras:.2f}')
print(f'Temos {somaMaiorMil} produtos acima de R$1000,00')
print(f'{nomeProduto} é o produto mais barato preço é R${menorPreco:.2f}')
print('\n--------------------------------------')







