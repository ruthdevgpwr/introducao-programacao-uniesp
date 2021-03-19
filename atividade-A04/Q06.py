numero1 = float(input('Digite o 1º número: '))
numero2 = float(input('Digite o 2º número: '))
numero3 = float(input('Digite o 3º número: '))
numero4 = float(input('Digite o 4º número: '))
numero5 = float(input('Digite o 5º número: '))

quantidade_maiores_10 = 0

if numero1 > 10:
    quantidade_maiores_10 = quantidade_maiores_10 + 1
if numero2 > 10:
    quantidade_maiores_10 = quantidade_maiores_10 + 1
if numero3 > 10:
    quantidade_maiores_10 = quantidade_maiores_10 + 1
if numero4 > 10:
    quantidade_maiores_10 = quantidade_maiores_10 + 1
if numero5 > 10:
    quantidade_maiores_10 = quantidade_maiores_10 + 1

print("A quantidade de números maiores que 10 é: " + str(quantidade_maiores_10))
