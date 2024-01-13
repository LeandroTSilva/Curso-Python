"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

"""

print('=-=' * 20)
print(' Programa Minha Casa, Minha Divída')
print('=-=' * 20)

valorCasa = float(input('Digite o valor da casa \n'))
salarioComprador = float(input('Digite agora o seu salário \n'))
anosPagamento = float(input('Em quantos anos prentende pagar? \n'))

valorFianciamento = valorCasa / (anosPagamento * 12)

terceiraParte = (salarioComprador * 30) / 100

if valorFianciamento <= terceiraParte:
    print(' *** APROVADO *** ')
    print('Prazo do financimento {:.0f} anos, valor das Parcelas R${:.2f}'.format(anosPagamento, valorFianciamento))
else:
    print(' *** EMPRESTIMO NEGADO ***')
    print('Motivo: Renda Baixa')