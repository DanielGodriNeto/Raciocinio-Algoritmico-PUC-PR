# Tarefa Calculdadora.
# Com prioridade PEMDAS.

input = input("Digite a expressão matemática: ")
try:
    resultado = eval(input)
    print(f"O resultado da expressão é: {resultado}")
except:
    print("Expressão inválida.")