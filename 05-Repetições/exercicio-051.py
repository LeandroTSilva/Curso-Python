"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

Quase consegui fazer este exercício, mas precisei da correção do professor Guanabara, isso porque me perdi em como calcular o decimo termo de uma PA
no código original eu fiz da seguinte forma:

valorPa = valorTermo + valorRazao

for c in range(1, 10):
   valorPa = valorPa + valorRazao
   print(valorPa)

exatamente neste ponto eu não soube como calcular a decimo termo da PA. então recorri a correção embora as progressões estivessem corretas, fugiam do que o enúnciado pedia.

"""


valorTermo = int(input('Digite o 1º termo \n'))
valorRazao = int(input('Digite agora a razão \n'))

# formula para calcula do décimo termo de uma PA
valoDecimo = valorTermo + (10 - 1) * valorRazao


for c in range(valorTermo, valoDecimo + valorRazao, valorRazao):
    print('{}'.format(c), end=('-> '))
print('Acabou!')   