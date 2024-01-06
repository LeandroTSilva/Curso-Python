'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. 
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

'''

from random import shuffle

primeiroAluno = str(input(' Nome do primeiro aluno \n'))
segundoAluno =  str(input(' Nome do segundo aluno \n'))
terceiroAluno = str(input(' Nome do tercerio aluno \n'))
quartoAluno = str(input(' Nome do quarto aluno \n'))

sequenciaGerada = [primeiroAluno, segundoAluno, terceiroAluno, quartoAluno]

shuffle(sequenciaGerada)

print( ' *** ' * 20)
print('A ordem de apresentação será a seguinte: {}'.format(sequenciaGerada))



