"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

somaIdade = 0
mediaIdade = 0
maiorIdadeMasculino = 0
nomeMasculinoMaiorIdade = ''
totalMulheresMenor20 = 0

for c in range(1, 5):
    nomeCadastro = str(input('Nome da {}ª pessoa\n'.format(c))).strip()
    idadeCadastro = int(input('Qual a idade? \n'))
    sexoCadastro = str(input('Qual o gênero [F]Feminino [M] Masculino \n')).strip().lower()


    somaIdade = somaIdade + idadeCadastro
    mediaIdade = somaIdade / 4

    if c == 1 and sexoCadastro in 'm':
        maiorIdadeMasculino = idadeCadastro
        nomeMasculinoMaiorIdade = nomeCadastro


    if sexoCadastro in 'm' and idadeCadastro > maiorIdadeMasculino:
        maiorIdadeMasculino = idadeCadastro
        nomeMasculinoMaiorIdade = nomeCadastro


    if sexoCadastro in 'f' and idadeCadastro <= 20:
        totalMulheresMenor20 += 1



print('-=' * 20)
print('A média de idade é {}'.format(mediaIdade))
print('O homem mais velho é o {} e sua idade é {}'.format(nomeMasculinoMaiorIdade, maiorIdadeMasculino))
print('Total de mulheres menor de 20 anos é {} e elas são: {}'.format(totalMulheresMenor20))
