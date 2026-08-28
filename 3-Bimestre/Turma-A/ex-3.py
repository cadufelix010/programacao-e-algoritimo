n = int(input('Escolha um número inteiro positivo: '))
contador = 1

if n > 0:
    while contador <= n:
        print(contador)
        contador += 1
else:
    print('Número inválido')
