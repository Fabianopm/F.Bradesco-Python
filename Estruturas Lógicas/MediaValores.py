qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while valor > 0.0:
    soma = soma + valor
    qtd = qtd + 1
    # entrada de valores
    valor = float(input("Digite um valor: "))

# caso digite um valor negativo o laço vai se encerrar
media = soma / qtd
print("\n Total da Soma: ", soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: %.2f" % media)
