positivos = 0
negativos = 0
zeros = 0
contador = 1

while contador <= 10:
    n = int(input('Digite um número: '))

    if n > 0:
        positivos = positivos + 1
    elif n < 0:
        negativos = negativos + 1
    else:
        zeros = zeros + 1

    contador = contador + 1

print('Positivos:', positivos)
print('Negativos:', negativos)
print('Zeros:', zeros)
