# Operação com dois números

n1 = float(input())
n2 = float(input())
operacao = input()

if operacao == "+":
    resultado = n1 + n2
    print(f"Você escolheu a operação de adição. O resultado dessa adição é {resultado:.2f}")

elif operacao == "-":
    resultado = n1 - n2
    print(f"Você escolheu a operação de subtração. O resultado dessa subtração é {resultado:.2f}")

elif operacao == "*":
    resultado = n1 * n2
    print(f"Você escolheu a operação de multiplicação. O resultado dessa multiplicação é {resultado:.2f}")

elif operacao == "/":
    resultado = n1 / n2
    print(f"Você escolheu a operação de divisão. O resultado dessa divisão é {resultado:.2f}")