# Eu pago ou não Imposto de Renda?

valor_diaria = float(input())
dias_trabalhados = int(input())

salario_bruto = valor_diaria * dias_trabalhados

if salario_bruto <= 2000.00:
    print("Você está isento do Imposto de Renda.")
    print(f"Seu salário é: R$ {salario_bruto:.2f}")

elif salario_bruto <= 5000.00:
    ir = salario_bruto * 0.15
    salario_liquido = salario_bruto - ir
    print("Você não está isento do Imposto de Renda.")
    print(f"Seu salário bruto é de: R$ {salario_bruto:.2f}")
    print(f"Seu valor do IR é: R$ {ir:.2f}")
    print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")

else:
    ir = salario_bruto * 0.275
    salario_liquido = salario_bruto - ir
    print("Você não está isento do Imposto de Renda.")
    print(f"Seu salário bruto é de: R$ {salario_bruto:.2f}")
    print(f"Seu valor do IR é: R$ {ir:.2f}")
    print(f"Seu salário líquido é de: R$ {salario_liquido:.2f}")