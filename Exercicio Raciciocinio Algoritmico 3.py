# Exercicio 3 Raciciocinio Algoritmico

#1. Exercicio Floresta
#Voce esta em uma floresta e precisa encontra um caminho pra seguir (Esquerda) ou (Direita)
#Caminho da Esqeurda voce encontra um rio que voce decide entre (Atravessar) ou (voltar)
#Se atravessar voce chega em uma vila segura
#Se voltar Voce permanece perdido na floresta

#Caminho da Direita voce encontra uma montanha que voce pode (Subir) ou (voltar)
#Se subir voce subir voce encontra um tesouro no topo
#Se voltar voce permanece perdido na floresta

#desafio pegar input usuario e mostrar resultado final

print("Você está em uma floresta, você pode ir para esquerda ou direita")
escolha1 = input("Escolha 'esquerda' ou 'direita': ").lower()

if escolha1 == "esquerda":
    print("Você encontrou um rio, você pode atravessar ou voltar")
    escolha2 = input("Escolha 'atravessar' ou 'voltar': ").strip().lower()
    
    if escolha2 == "atravessar":
        print("Você chegou em uma vila segura")
    elif escolha2 == "voltar":
        print("Você voltou e permanece perdido na floresta")
    else:
        print("Opção inválida. Voce permanece perdido na floresta")

elif escolha1 == "direita":
    print("Você encontrou uma montanha, você pode subir ou voltar")
    escolha2 = input("Escolha 'subir' ou 'voltar': ").strip().lower()
    
    if escolha2 == "subir":
        print("Você encontrou um tesouro no topo")
    elif escolha2 == "voltar":
        print("Você voltou e permanece perdido na floresta")
    else:
        print("Opção inválida. Voce permanece perdido na floresta")


# Exercicio 2
# Pegue um numero do usuuario
# Verifique se esta entre 10 e 50 (inclusive)
# Se e menor que 10
# Se e maior que 50

numero = int(input("Digite um número: "))
if 10 <= numero <= 50:
    print("O número está entre 10 e 50 (inclusive)")
elif numero < 10:
    print("O número é menor que 10")
else:
    print("O número é maior que 50")


#Pede um ano e verifica se é bissexto
# For divisivel por 4 e nao divisivel por 100 ou for divisivel por 400
ano = int(input("Digite um ano: "))
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")

# Peca usuario e senha
#autoriza se o usuario for "adimin" e a senha for "1234"
#se o usuario for "convidado" e nao digitar senha exiba acesso restrito
#caso contrario exiba acesso negado

usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")
if usuario == "admin" and senha == "1234":
    print("Acesso autorizado")
elif usuario == "convidado" and senha == "":
    print("Acesso restrito")
else:
    print("Acesso negado")

# Peca duas coordenadas (x e y) e verifique a posicao do ponto em relacao a um quadrado cujos verices vao de (0,0) a (10,10)
# se o ponmto estiver estritamento dentro da regiao mostre "Dentro do quadrado"
# se o ponto estiver na borda do quadrado mostre "Na fronteira"
# se o ponto estiver fora do quadrado mostre "Fora do quadrado"

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))
if 0 < x < 10 and 0 < y < 10:
    print("Dentro do quadrado")
elif (x == 0 or x == 10) and 0 <= y <= 10 or (y == 0 or y == 10) and 0 <= x <= 10:
    print("Na fronteira")
else:
    print("Fora do quadrado")

# DESAFIO!!!
# Peca tres lados de uma figura. PRimeiro verifique se os lados podem formar um triangulo
# Se um deles for maior que a soma dos outros dois
# Se puderem formar um triangulo, verifique se e equilatero isoceles ou escaleno

lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))
if (lado1 < lado2 + lado3) and (lado2 < lado1 + lado3) and (lado3 < lado1 + lado2):
    if lado1 == lado2 == lado3:
        print("O triângulo é equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("O triângulo é isósceles")
    else:
        print("O triângulo é escaleno")