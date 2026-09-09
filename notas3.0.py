count = 1
sum_m = 0
while True:
    name = str(input(f'\nNome do {count}º aluno (ou exit para sair): '))

    if name.lower() == 'exit':
        print('PROGRAMA ENCERRADO!')
        break #quebra o resto do código

    print(50 * '-')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))

    if (n1 > 10 or n2 > 10 or n3 > 10):
        print('NOTA INVALIDA! Não existem notas maiores que 10')
        continue #continua a estrutura em vez de quebrar ela que nem o 'break'
        
    print(50 * '-')

    media = (n1 + n2 + n3) /3
    sum_m += media

    if (media >= 7.0):
        print(f'O aluno {name} foi APROVADO com a média {media:.2f}')

    else:
        print(f'O aluno {name} foi REPROVADO com a média {media:.2f}')

    count += 1 #contador que vai ser somado a cada aluno