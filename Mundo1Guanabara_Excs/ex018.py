from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tg = tan(radians(angulo))

print('Ângulo {}°'.format(angulo))
print('Seno -> {:.2f}'.format(seno))
print('Cosseno -> {:.2f}'.format(cosseno))
print('Tangente -> {:.2f}'.format(tg))