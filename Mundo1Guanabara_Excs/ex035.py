print('-=-'*15)
print('Analisador de Triângulos')
print('-=-'*15)
l1 = float(input('Digite o valor do primeiro segmento: '))
l2 = float(input('Digite o valor do segundo segmento: '))
l3 = float(input('Digite o valor do terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima não podem formar triângulo!')