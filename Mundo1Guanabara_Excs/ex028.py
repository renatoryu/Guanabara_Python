import random
from time import sleep
cpu = random.randrange(0,5)
print('\033[0;33;40m-=-\033[m' *20)
print('\033[0;36;40mVou pensar em um número entre 0 e 5. Tente adivinhar...\033[m')
print('\033[0;33;40m-=-\033[m' *20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == cpu:
    print('\033[1;32;40mVocê acertou, parabéns!\033[m')
else:
    print('\033[1;31;40mVocê errou!\033[m')
    print('\033[1;31;40mA CPU tinha escolhido o número {}\033[m'.format(cpu))
