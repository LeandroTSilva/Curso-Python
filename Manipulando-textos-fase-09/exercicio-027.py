'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

'''

nomeCompleto = str(input('Digite seu nome completo \n')).strip()
seuNome = nomeCompleto.split()
print('Seu primeiro nome é {}'.format(seuNome[0]))
print('Seu último nome é {}'.format(seuNome[len(seuNome) - 1]))



