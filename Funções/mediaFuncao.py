def lernotas():
    n = float(input("Digite uma nota para o aluno(a): "))
    return n


def resultado(n1, n2):
    media = (n1+n2) / 2
    print("Nota 1: %.2f " % n1)
    print("Nota 2: %.2f " % n2)
    print("Média: %.2f " % media)
    if media >= 7:
        print("Aprovado com média: %.2f " % media)
    else:
        print("Reprovado com média: %.2f " % media)


a = lernotas()
b = lernotas()
resultado(a, b)
