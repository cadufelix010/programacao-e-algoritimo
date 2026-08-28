n = int(input('Digite um número positivo: '))
contador = 1

if n > 0:
    while contador <= n:
        print(contador)
        contador = contador + 1
else:
    print('Número inválido')
