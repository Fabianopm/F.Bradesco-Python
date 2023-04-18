notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

# Calculando a media
mediaFinal = (notaA + notaB) / 2

# Verificação
if mediaFinal >= 7.0:
    print("Aluno aprovado com média: %2.f" % mediaFinal)
else:
    print("Aluno reprovado com média: %2.f" % mediaFinal)
