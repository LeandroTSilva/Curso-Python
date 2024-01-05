'''
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

'''
grauCelsiu = float(input('Digite a temperatura em graus Celsisus (C°) \n'))

grauFahrenheit = (grauCelsiu * 1.8) + 32

print(' * ' * 40)
print(' a temperatura em {}C° corresponde a {}F°'.format(grauCelsiu, grauFahrenheit))
