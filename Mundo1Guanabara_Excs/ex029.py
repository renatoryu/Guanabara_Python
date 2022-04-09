velocidade = float(input('Digite a velocidade do carro: '))
if velocidade > 80:
    print('Você foi multado por estar à {}km em uma pista de 80Km/h'.format(velocidade))
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')