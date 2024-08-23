"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos. 

"""
menorIdade = 0
parar = True
contHomem = 0
contMulherMenor20 = 0

while parar == True:
    idade = int(input('Olá qual sua idade \n'))
    sexo = input('Qual o seu sexo? [M] - Masculino / [F] - Feminino \n').strip().lower()[0]

    if idade < 18:
        menorIdade += 1

    if sexo == 'm':
        contHomem += 1

    if sexo == 'f' and idade < 20:
        contMulherMenor20 += 1


    parar = input('Deseja fazer um novo cadastro? S-Sim | N-Não \n').strip().lower()[0]
    if parar == 's':
        parar = True
    elif parar == 'n':
        para = False

print(f'Temos {menorIdade} pessoas, menores de 18 anos de idade')
print(f'Total homens cadastrados: {contHomem}')
print(f'Mulheres com menos de 20 anos somam: {contMulherMenor20}')








