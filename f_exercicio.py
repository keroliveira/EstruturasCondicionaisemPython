# Par, Ímpar, Positivo, Negativo

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

pares_positivos = ""
pares_negativos = ""
impares_positivos = ""
impares_negativos = ""
zeros = ""

for n in [n1, n2, n3, n4]:
    if n == 0:
        zeros += f"{n}\n"
    elif n % 2 == 0 and n > 0:
        pares_positivos += f"{n}\n"
    elif n % 2 == 0 and n < 0:
        pares_negativos += f"{n}\n"
    elif n % 2 != 0 and n > 0:
        impares_positivos += f"{n}\n"
    else:
        impares_negativos += f"{n}\n"

print("Números pares e positivos:")
print(pares_positivos)

print("Números pares e negativos:")
print(pares_negativos)

print("Números ímpares e positivos:")
print(impares_positivos)

print("Números ímpares e negativos:")
print(impares_negativos)

print("Números zeros:")
print(zeros)