'''
 Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

'''

seuNome = str(input(' Digite seu nome completo \n')).strip()
seuNome.find('Silva', 0)
seuNome.capitalize()
print('Seu Nome tem Silva? {}'.format('Silva' in seuNome))