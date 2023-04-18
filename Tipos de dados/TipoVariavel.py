codigo = 10
salario = 1500.00
nome = 'Fabiano'
situacao = True

tipo = type(salario)  # "type" para verificar o tipo do dado

print(salario)
print(tipo)

print("-------------------------------------------------------------------------")

# concatenação com virgula
# para apresentaçã ode textos é ncessaário usar aspas duplas " ".
print("Código:", codigo, "Nome:", nome, "O salário atual é de R$:", salario)

print("-------------------------------------------------------------------------")

# Também podemos concatenar as informações na linguagem Python utilizando o sinal de soma (+).
# Neste caso, temos de converter os valores que não são string para o tipo string.
# Para isso, utilizamos o comando (str) antes da impressão da variável

print("Código:" + str(codigo) + " Nome:" + nome + " O salário é de R$:" + str(salario))

