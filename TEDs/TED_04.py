idade = int(input('--- IDENTIFICAÇÃO DA CATEGORIA DO NADADOR --- \n\
Nadador, por favor, informe a sua idade para saber em qual categoria você se encaixa: '))

tamanho_barra = 60
print(tamanho_barra * '=')
mensagem = 'Nadador, você se encaixa na seguinte categoria:'

if 5 <= idade <= 7:
    print(mensagem + 'INFANTIL A')
elif 8 <= idade <= 10:
    print(mensagem + 'INFANTIL B')
elif 11 <= idade <=13:
    print(mensagem + 'JUVENIL A')
elif 14 <= idade <= 17:
    print(mensagem + 'JUVENIL B')
elif idade >= 18:
    print(mensagem + 'SÊNIOR')

print(tamanho_barra * '=')
