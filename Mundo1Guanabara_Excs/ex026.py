frase = str(input('Digite uma frase qualquer: ')).upper().strip()
letraa = frase.count('A')
print('A letra A apareceu {} vezes'.format(letraa))

primeiravez = frase.find('A')+1
print('A primeira letra A apareceu na posição {}'.format(primeiravez))

ultimavez = frase.rfind('A')+1
print('A última letra A apareceu na posição {}'.format(ultimavez))