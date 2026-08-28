contador = 1
soma = 0

n = int(input('Digite um número positivo: '))
if n > 0:
    while contador <= n:
        if contador % 2 == 0:
            soma += contador
        contador += 1
    print(f'A soma dos números pares é: {soma}')
else:
    print('Número inválido')
