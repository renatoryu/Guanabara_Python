frase = 'Curso em Vídeo Python'
print(frase[9::2])

#? len - contar quantidade de letras
print(len(frase))

#! cont - contar letras específicas
cont = frase.count('o')
print(cont)

#* find - encontrar palavras
encontrar = frase.find('Android')
print(encontrar)

#in - existe
existe = 'Curso' in frase
print(existe)

#! replace - reposicionar palavras
trocar = frase.replace('Python','Android')
print(trocar)

#? - Em maiúsculas, minúsculas, capitalizadas e título
maiusculas = frase.upper()
print(maiusculas)

minusculas = frase.lower()
print(minusculas)

capitalizada = frase.capitalize()
print(capitalizada)

titulo = frase.title()
print(titulo)

#! split - dividir com os espaços
dividir = frase.split()
print(dividir[2][3])

# join - juntar palavras
juntar = '-'.join(dividir)
print(juntar)

#* strip - remover espaços inúteis
# rstrip - direita
# lstrip - esquerda

frase = '   Aprenda Python!   '
remover = frase.strip()
print(remover)
