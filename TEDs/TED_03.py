nota_1 = float(input("Nota 1:"))
peso_1 = float(input("Peso 1:"))

nota_2 = float(input("Nota 2:"))
peso_2 = float(input("Peso 2:"))

nota_3 = float(input("Nota 3:"))
peso_3 = float(input("Peso 3:"))

nota_4 = float(input("Nota 4:"))
peso_4 = float(input("Peso 4:"))

# calcula a média
media = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3 + nota_4 * peso_4) / (peso_1 + peso_2 + peso_3 + peso_4)

print("A Média é: ", media)
