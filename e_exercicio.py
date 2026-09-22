# É triângulo é? Que triângulo é?

lado_1 = int(input())
lado_2 = int(input())
lado_3 = int(input())

# Verifica se forma um triângulo
if (lado_1 + lado_2 > lado_3) and (lado_1 + lado_3 > lado_2) and (lado_2 + lado_3 > lado_1):
    
    # Classifica o triângulo
    if lado_1 == lado_2 == lado_3:
        print("Triangulinho com todos os lados iguais: é equilátero!!")
    
    elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
        print("Triangulinho com dois lados iguais: é isósceles!!")
    
    else:
        print("Tem os três lados diferentes mas ainda continua sendo um triangulinho: é escaleno!!")

else:
    print("Esses segmentos de reta não formam um triângulo. Tchau!!!!")