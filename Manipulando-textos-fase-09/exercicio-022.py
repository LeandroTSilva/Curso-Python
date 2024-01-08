'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.

'''



nomeCompleto = str(input('Digite seu nome completo \n'))

print('Seu nome em maiúsculas é {}'.format(nomeCompleto.upper()))
print('Seu nome em minúscula é {}'.format(nomeCompleto.lower()))

nomeSemEspaco = len(nomeCompleto) - nomeCompleto.count(' ')

# Alternativa nomeSemEspaco = nomeCompleto.replace(" ","")
print('Seu nome completo tem ao todo {} letras'.format(nomeSemEspaco))

primeiroNome = nomeCompleto.split()
print('O seu primeiro nome é {} e tem {} letras'.format(primeiroNome[0], (len(primeiroNome[0]))))
















