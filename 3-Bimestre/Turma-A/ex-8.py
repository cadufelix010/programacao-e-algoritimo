divisor = 1
quantidade = 0

n = int(input('Digite um número inteiro positivo: '))

if n > 0:
    while divisor <= n:
        if n % divisor == 0:
            quantidade += 1
        divisor += 1

    if quantidade == 2:
        print(f'O número {n} é primo')
    else:
        print(f'O número {n} não é primo')
else:
    print('Número inválido')
