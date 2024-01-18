"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.


"""
valorPar = 0
contEntrada = 0
contPar = 0

for c in range(1, 7):
    valorEntrada = int(input("Digite o {}º valor \n".format(c)))
    contEntrada += 1
    if valorEntrada % 2 == 0:
        valorPar = valorPar + valorEntrada
        contPar += 1
        
print('O total de entradas foi: {}, numeros pares foram {} e a soma de todos pares é: {}'.format(contEntrada, contPar, valorPar))