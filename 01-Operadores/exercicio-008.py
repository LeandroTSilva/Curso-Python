'''
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

'''

valorMetro = float(input(' Digite um valor em metros (m) \n'))

valorDam = valorMetro * 10
valorHm = valorDam * 10
valorKm = valorHm * 10

valorCm = valorMetro / 10
valorDm = valorCm / 10
valorMm = valorDm / 10


print(' - ' * 40)

print(' O valor de {}m em Decametros é {}dam'.format(valorMetro, valorDam))
print(' O valor de {}m em Hectomêtro é {}hm'.format(valorMetro, valorHm))
print(' O valor de {}m em Quilomêtro é {}km'.format(valorMetro, valorKm))
print(' O valor de {}m em Centimêtros é {}cm'.format(valorMetro, valorCm))
print(' O valor de {}m em Decimêtro é {}dm'.format(valorMetro, valorDm))
print(' O valor de {}m em Milimêtros é {}mm'.format(valorMetro, valorMm))
1
print(' - ' * 40)


