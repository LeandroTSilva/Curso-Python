"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros

"""



print('=-=' * 20)
print(' *** Magazine Curso em vídeo *** ')
print('=-=' * 20)


valorProduto = float(input('Qual o valor do Produto? (R$) '))
formaPgto = int(input("""
Escolha a forma de Pagamento:
      [1] => A vista dinheiro/cheque:
      [2] => A vista no cartão:
      [3] => 2x cartão:
      [4] => 3x no cartão:
 """))

if formaPgto == 1:
    desconto = valorProduto - (valorProduto * 10) / 100
    print('10% de desconto aplicado, total a pagar é R${:.2f}'.format(desconto))
elif formaPgto == 2:
    desconto = valorProduto - (valorProduto * 5)/ 100
    print('5% de desconto aplicado, total a pagar é R${:.2f}'.format(desconto))
elif formaPgto == 3:
    parcela = valorProduto / 2
    print('Valor Total {:.2f}, parcelas: 2 de R${:.2f}'.format(valorProduto, parcela))
elif formaPgto == 4:
    numeroParcela = float(input('Quantas parcelas? '))
    valorPrazo = valorProduto + (valorProduto * 20) / 100
    parcela = valorPrazo / numeroParcela
    print('Total a prazo R${:.2f}, 3 parcelas de R${:.2f}'.format(valorPrazo, parcela))
else:
    print(">>> Opção inválida ! tente de novo <<< ")