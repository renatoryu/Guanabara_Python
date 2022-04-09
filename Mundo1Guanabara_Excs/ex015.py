km = float(input('Digite a quantidade de quilômetros percorridos: '))
dias = int(input('Digite a quantidade de dias alugados com o carro: '))
precodia = 60*dias
precokm = 0.15*km
print('Percorreu {}km e utilizou o carro por {} dia(s), o preço a pagar é de R${:.2f}'.format(km,dias,precodia+precokm))