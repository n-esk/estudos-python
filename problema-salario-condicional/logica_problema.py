# checar se salario é menor do que o minimo
salario_minimo = 1200
salario = int(input("Digite seu salario: "))

if salario < salario_minimo:
    print("Seu salário tá abaixo do minimo")
elif salario == salario_minimo:
    print("Seu salário é igual ao salário mínimo")
elif salario > 3 * salario_minimo:
    print("")
else:
    print("Seu salário é maior do que o salário minimo")
