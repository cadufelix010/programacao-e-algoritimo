n = int(input('Digite um número: '))
fatorial = 1
contador = 1

if n >= 0:
    while contador <= n:
        fatorial = fatorial * contador
        contador = contador + 1
    print('Fatorial:', fatorial)
else:
    print('Número inválido')
