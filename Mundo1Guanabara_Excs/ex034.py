salario = float(input('Digite seu salário: R$'))
if salario > 1250:
    salarionovo = salario + salario*0.10
else:
    salarionovo = salario + salario*0.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salario,salarionovo))