'''
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

'''

valorCidade = str(input('Em que cidade você Nasceu?\n')).strip()
valorCidade.find('Santo', 0)
valorCidade = valorCidade.capitalize()
print('Santo' in valorCidade)


