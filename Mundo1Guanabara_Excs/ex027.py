nome = str(input('Digite seu nome completo: ')).strip()
nome_dividido = nome.split()
print(nome_dividido[0],nome_dividido[-1])
print('Primeiro nome: {}'.format(nome_dividido[0]))
print('Último nome: {}'.format(nome_dividido[-1]))
