"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 08 - Número primo
"""

numero = int(input("Digite um número inteiro positivo: "))
divisor = 1
quantidade_divisores = 0

if numero > 0:
    while divisor <= numero:
        if numero % divisor == 0:
            quantidade_divisores += 1
        divisor += 1

    if quantidade_divisores == 2:
        print("O número é primo.")
    else:
        print("O número não é primo.")
else:
    print("Número inválido.")
