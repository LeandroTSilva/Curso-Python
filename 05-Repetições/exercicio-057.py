"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
valorGenero = str(input('Informe seu sexo [M/F] \n')).strip().upper()[0]

while valorGenero not in 'MF':
    valorGenero = str(input('DADOS INVÁLIDOS! por favor informe corretamente \n')).strip().upper()[0]
print('=-' * 20)
print('DADOS ENVIADOS COM SUCESSO')
