contador = 1
fatorial = 1

n = int(input('Digite um número inteiro positivo: '))

if n >= 0:
    while contador <= n:
        fatorial *= contador
        contador += 1
    print(f'Fatorial: {fatorial}')
else:
    print('Número inválido')
