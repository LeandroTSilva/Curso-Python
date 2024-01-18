"""
 Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

Não consegui fazer este exercício, pois travei nos acumuladores, preciso treinar mais exercicios como este conceito de acumuladores


"""

total = 0
cont = 0
for c in range(1, 501, 2):
   if c % 3 == 0:
      total = total + c
      cont = cont + 1
print('A soma de todos os {} solicitados é {}'.format(cont, total))