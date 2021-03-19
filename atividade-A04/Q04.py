print('--- IDENTIFICAÇÃO DA CATEGORIA DO NADADOR ---')
idade = int(input('Nadador, por favor, informe a sua idade para saber em qual categoria você se encaixa: '))

if idade >= 5 and idade <= 7:
    print('Nadador, você se encaixa na seguinte categoria: INFANTIL A')
elif idade >= 8 and idade <=10:
    print('Nadador, você se encaixa na seguinte categoria: INFANTIL B')
elif idade >= 11 and idade <=13:
    print('Nadador, você se encaixa na seguinte categoria: JUVENIL A')
elif idade >= 14 and idade <= 17:
    print('Nadador, você se encaixa na seguinte categoria: JUVENIL B')
elif idade >= 18:
    print('Nadador, você se encaixa na seguinte categoria: SÊNIOR')