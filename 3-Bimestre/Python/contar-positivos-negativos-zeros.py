"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 07 - Contador de positivos, negativos e zeros
"""

positivos = 0
negativos = 0
zeros = 0
contador = 1

while contador <= 10:
    numero = int(input(f"Digite o {contador}º número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

    contador += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Zeros:", zeros)
