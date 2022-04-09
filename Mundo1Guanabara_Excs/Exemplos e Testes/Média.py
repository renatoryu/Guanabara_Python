notaA = float(input("Digite o valor da nota 1: "))
notaB = float(input("Digite o valor da nota 2: "))

# calcularmédia
mediafinal = (notaA+notaB)/2

# verificação
if mediafinal >= 7.0:
    print(" A média: %.2f - Aprovado" % mediafinal)
else:
    print(" A média: %.2f - Reprovado" % mediafinal)
