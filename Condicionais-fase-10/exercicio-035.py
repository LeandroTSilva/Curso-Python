"""
 Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

"""

reta1 = float(input('Digite a reta 1 \n'))
reta2 = float(input('Digite a reta 2 \n'))
reta3 = float(input('Digite a reta 3 \n'))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('Com os valores {}, {} e {} é possível ter um triângulo'.format(reta1, reta2, reta3))
else:
    print('Com os valores {}, {} e {} NÃO possível obter um triângulo'.format(reta1, reta2, reta3))
print(' **** Fim do Programa **** ')
