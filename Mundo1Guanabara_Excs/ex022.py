nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em letras maiúsculas é {}'.format(nome.upper()))
print('Seu nome completo em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))

