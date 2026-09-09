for i in range(100) :
    name = str(input(f'\nNome do {i+1}º aluno: '))
    print(20 * '-')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    n3 = float(input('Nota 3: '))
    print(20 * '-')

    media = (n1 + n2 + n3) /3

    if (media >= 7.0):
        print(f"O aluno {name} foi APROVADO com a média {media:.2f}")

    else:
        print(f"O aluno {name} foi REPROVADO com a média {media:.2f}")