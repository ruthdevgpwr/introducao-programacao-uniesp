print('--- SITUAÇÃO ACADÊMICA ---')
nota1 = float(input('Informe a sua 1ª nota: '))
nota2 = float(input('Informe a sua 2ª nota: '))
media = (nota1 + nota2)/2

if media >= 7:
    print(f'Aluno está APROVADO com média {media}')
elif media < 4:
    print(f'Aluno está REPROVADO com média {media}')
else:
    print(f'Aluno está APTO A FINAL com média {media}')
