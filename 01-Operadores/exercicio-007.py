'''
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

'''

nota1 = float(input(' Digite a primeira nota \n'))
nota2 = float(input(' Digite a segunda nota \n'))

mediaFinal = (nota1 + nota2) / 2

print(' - ' * 40)
print(' A média final é {:.2f}'.format(mediaFinal))
print(' - ' * 40)

