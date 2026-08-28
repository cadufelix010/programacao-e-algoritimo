contador = 1
n = int(input('Digite um número de 1 a 10: '))

if n >= 1 and n <= 10:
    while contador <= 10:
        print(f'{n} x {contador} = {n * contador}')
        contador += 1
else:
    print('Número inválido')
