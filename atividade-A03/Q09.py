valor = float(input('Informe o valor da prestação: '))
taxa = float(input('Informe a taxa: '))
tempo = float(input('Informe o tempo: '))

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f' O valor da prestacao em atraso é: R$ {prestacao} ')
