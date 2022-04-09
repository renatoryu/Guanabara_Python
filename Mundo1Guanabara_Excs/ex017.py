from math import hypot
catop = float(input('Digite o valor do cateto oposto: '))
catadj = float(input('Digite o valor do cateto adjacente: '))
print('Com o cateto oposto valendo {} e o cateto adjacente valendo {}, a hipotenusa irá valer: {:.2f}'.format(catop,catadj,hypot(catop,catadj)))