"""
DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes




Antes de conferir a correção, eu de fato fiz todas as possibilidades checando se segmento1 == segmento2 != segmento3 or etc...
o programa funcionou, mas a alternativa mais curta do professor Guanabara fez mais sentindo e optei por usá-la, pois deixa o código mais limpo
"""

print('=-=' * 20)
print(' *** Curso Em Vídeo Geometria 2.0 *** ')
print('=-=' * 20)

segmento1 = float(input('Digite um segmento \n'))
segmento2 = float(input('Digite o segundo segmento \n'))
segmento3 = float(input('Digite o terceiro segmento \n'))

if segmento1 < segmento2 + segmento3 and segmento2 < segmento1 + segmento3 and segmento3 < segmento1 + segmento2:
    print('É possivél obter um triângulo:',end=(''))
    if segmento1 == segmento2 == segmento3:
        print('EQUILÁTERO')
    elif segmento1 != segmento2 != segmento3 != segmento1:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('>>> NÃO É POSSÍVEL OBTER UM TRIÂNGULO <<<')


