n = int(input('Digite um número de 1 a 10: '))
contador = 1

if n >= 1 and n <= 10:
    while contador <= 10:
        print(n, 'x', contador, '=', n * contador)
        contador = contador + 1
else:
    print('Número inválido')
