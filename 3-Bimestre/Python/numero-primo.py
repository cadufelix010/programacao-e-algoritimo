n = int(input('Digite um número positivo: '))
divisor = 1
quantidade = 0

if n > 0:
    while divisor <= n:
        if n % divisor == 0:
            quantidade = quantidade + 1
        divisor = divisor + 1

    if quantidade == 2:
        print('É primo')
    else:
        print('Não é primo')
else:
    print('Número inválido')
