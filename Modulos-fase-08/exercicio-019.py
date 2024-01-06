'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

'''

from random import choice

primeiroAluno = input(' Digite o nome do primeiro aluno \n')
segundoAluno = input('Digite o nome do segundo aluno \n')
terceiroAluno = input('Digite o nome do terceiro aluno \n')
quartoAluno = input('Digite o nome do quarto aluno \n')

alunoSorteado = choice([primeiroAluno, segundoAluno, terceiroAluno, quartoAluno])

print(' *** ' * 10)
print('O Aluno(a) sorteado para apagar a lousa é... {}'.format(alunoSorteado))
print(' *** ' * 10)

