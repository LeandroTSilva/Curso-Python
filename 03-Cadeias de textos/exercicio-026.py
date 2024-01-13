'''
 Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.



    *** Abaixo a versão original que leva em considerção a contagem do Python começando do 0 (zero)

    print('A frase acima tem {} letras (a)'.format(fraseEntrada.count('a')))
    print('A primeira letra A esta na posição {}'.format(fraseEntrada.find('a', 0)))
    print('A última letra A esta na posição {}'.format(fraseEntrada.rfind('a')))


'''

fraseEntrada = str(input(' Digite uma frase curta \n')).strip()
fraseEntrada = fraseEntrada.lower()
print('A frase acima tem {} letras (a)'.format(fraseEntrada.count('a')))
print('A primeira letra A esta na posição {}'.format(fraseEntrada.find('a', 0) + 1))
print('A última letra A esta na posição {}'.format(fraseEntrada.rfind('a') + 1))


