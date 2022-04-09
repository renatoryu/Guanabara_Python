km = float(input('Digite a distância da viagem em quilômetros: '))
if km <= 200:
    valor = 0.50*km
    print('O preço da passagem vai ser R${:.2f}, {}km '.format(valor,km))
else:
    valor = 0.45*km
    print('O preço da passagem vai ser R${:.2f}, {}km'.format(valor,km))