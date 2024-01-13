"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO

"""

print('=-=' * 20)
print(' *** Curso Em Vídeo *** ')
print('=-=' * 20)

nota1 = float(input('Digite a primeira nota \n'))
nota2 = float(input('Digite a segunda nota \n'))

mediaFinal = (nota1 + nota2) / 2

if mediaFinal < 5.0:
    print('A média final é {:.2f} *** REPROVADO ***'.format(mediaFinal))
elif mediaFinal >= 5.0 and mediaFinal <= 6.9:
    print('A média final é {:.2f} *** RECUPERAÇÃO ***'.format(mediaFinal))
elif mediaFinal >= 7.0:
    print('A média fina é {:.2f} *** APROVADO ***'.format(mediaFinal))
else:
    print('Entrada Inválida, tente de novo')