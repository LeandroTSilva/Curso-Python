"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida

"""


print('=-=' * 20)
print(' *** Curso Em Vídeo Medicina *** ')
print('=-=' * 20)


altura = float(input('Qual a sua altura? \n'))
peso = float(input('Qual seu peso? \n'))

valorIMC = peso / (altura * altura)

if valorIMC < 18.5:
    print('Seu IMC é {:.1f}: >>> Abaixo do peso <<< '.format(valorIMC))
elif valorIMC >= 18.5 and valorIMC < 25:
    print('Seu IMC é {:.1f}: >>> Peso Ideal <<< '.format(valorIMC))
elif valorIMC >= 25 and valorIMC < 30:
    print('Seu IMC é {:.1f}: >>> Sobrepeso <<<'.format(valorIMC))
elif valorIMC >= 30 and valorIMC < 40:
    print('Seu IMC é {:.1f}: >>> Obesidade <<<'.format(valorIMC))
else:
    print(' Seu IMC é {:.1f}: >>> Obesidade Morbida <<< '.format(valorIMC))