# Média Salarial: maior, menor ou a mesma?

media_salarial = float(input())
nome_funcionario = input()
salario_funcionario = float(input())

resultado = abs(salario_funcionario - media_salarial)

if salario_funcionario > media_salarial:
    print(f"{nome_funcionario} recebe R$ {resultado:.2f} a mais do que a média salarial da empresa.")

elif salario_funcionario < media_salarial:
    print(f"{nome_funcionario} recebe R$ -{resultado:.2f} a menos do que a média salarial da empresa.")

else:
    print(f"{nome_funcionario} recebe igual a média salarial da empresa.")