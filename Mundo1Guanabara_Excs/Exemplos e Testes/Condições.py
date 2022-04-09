n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 8.0:
    print('Parabéns pela sua nota!')
elif m >= 6.0: 
    print('Você foi bem mas pode melhorar!')
else:
    print('Precisa estudar mais!')