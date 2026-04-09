# #1 Tarefa basico do "for" em Python.

for i in range(1, 11):
    print(i)

for i in range(10, 0, -1):
    print(i)


# #2 Tarefa comparacao com "for" em Python.

for i in range(1, 11):
    if i % 2 != 0:
        print(f"{i} é ímpar.")
    else:
        print(f"{i} é par.")


# Peça ao usuário que digite uma palavra que comece com uma vogal
# e depois imprima cada letra em uma linha

while True:
    palavra = input("Digite uma palavra que comece com uma vogal: ")
    if palavra and palavra[0].lower() in "aeiou":
        break
    else:
        print("A palavra não começa com uma vogal. Tente novamente.")

for letra in palavra:
    print(letra)


# Números de 1 até 100 múltiplos de 3 e não múltiplos de 5 + contagem

contador = 0
for i in range(1, 101):
    if i % 3 == 0 and i % 5 != 0:
        print(i)
        contador += 1

print("Quantidade encontrada:", contador)


# Soma de 1 até n mostrando a expressão completa

while True:
    n = int(input("Digite um número inteiro positivo: "))
    if n > 0:
        break
    else:
        print("Número inválido. Tente novamente.")

soma = 0
expressao = ""

for i in range(1, n + 1):
    soma += i
    expressao += str(i)
    if i < n:
        expressao += " + "

expressao += f" = {soma}"
print(expressao)


# Tabuadas entre número inicial e final

while True:
    inicio = int(input("Digite um número inicial: "))
    fim = int(input("Digite um número final: "))
    if inicio <= fim:
        break
    else:
        print("Número inicial deve ser menor ou igual ao número final. Tente novamente.")

for i in range(inicio, fim + 1):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()


# Padrão de linhas com 1

while True:
    linhas = int(input("Digite a quantidade de linhas: "))
    if linhas > 0:
        break
    else:
        print("Número inválido. Tente novamente.")

for i in range(1, linhas + 1):
    print("1" * i)