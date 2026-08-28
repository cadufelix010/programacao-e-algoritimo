n = int(input('Digite um número positivo: '))
soma = 0
contador = 1

if n > 0:
    while contador <= n:
        if contador % 2 == 0:
            soma = soma + contador
        contador = contador + 1
    print('Soma dos números pares:', soma)
else:
    print('Número inválido')
