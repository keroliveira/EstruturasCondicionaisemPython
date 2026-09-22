# Número, vogal ou operação matemática

caractere = input()

# Verifica se é um número
if caractere.isnumeric():
    print("O caractere é um número")

# Verifica se é uma operação matemática
elif caractere in "+-*/":
    print("O caractere é uma operação matemática")

# Verifica se é uma vogal (maiúscula ou minúscula)
elif caractere.lower() in "aeiou":
    print("O caractere é uma vogal")