'''
 Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

'''

valorLargura = float(input('Digite a  largura da parede \n'))
valorAltura = float(input('Digite a altura da parede \n'))

valorArea = valorLargura * valorAltura

qntdTinta = valorArea / 2

print(' - ' * 40)

print(' A sua parede tem dimensão de {:.2f} x {:.2f} e área de {:.2f}m²'.format(valorLargura, valorAltura, valorArea))
print(' Para pintar esta você vai precisa de {}Lts de tinta'.format(qntdTinta))

print(' - ' * 40)


