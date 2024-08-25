"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$100 R$50, R$20, R$10, R$5 e R$2.

"""
print('-' * 30)
print('{:^30}'.format('CAIXA ELETRONICO'))
print('-' * 30)

valorSaque = int(input('Qual o valor a ser sacado R$'))
montante = valorSaque
cedulaAtual = 200
totalCedula = 0

while True:
   if montante >= cedulaAtual:
      montante -= cedulaAtual
      totalCedula += 1
   else:
      if totalCedula > 0:
        print(f'Total de cédulas {totalCedula} de R${cedulaAtual:.2f}')
      elif cedulaAtual == 200:
         cedulaAtual = 100
      elif cedulaAtual == 100:
         cedulaAtual = 50
      elif cedulaAtual == 50:
         cedulaAtual = 20
      elif cedulaAtual == 20:
         cedulaAtual = 10
      elif cedulaAtual == 10:
        cedulaAtual = 5
      elif cedulaAtual == 5:
         cedulaAtual = 2
      elif cedulaAtual == 2:
         cedulaAtual = 1
      totalCedula = 0

      if montante == 0:
         break

print('-' * 40)
print('{:^30}'.format('SAQUE EFETUADO COM SUCESSO, OBRIGADO'))
print('-' * 40)