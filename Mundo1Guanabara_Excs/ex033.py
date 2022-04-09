a = float(input('Digite um número: '))
b = float(input('Digite um segundo número: '))
c = float(input('Digite o último número: '))
#Verificando menor
menor = a 
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#Verificando maior
maior = a 
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
    
print('O maior valor digitado foi: {:.0f}'.format(maior))
print('O menor valor digitado foi: {:.0f}'.format(menor))