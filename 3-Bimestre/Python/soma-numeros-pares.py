"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 04 - Soma dos números pares
"""

numero = int(input("Digite um número inteiro positivo: "))
contador = 1
soma = 0

if numero > 0:
    while contador <= numero:
        if contador % 2 == 0:
            soma += contador
        contador += 1

    print("Soma dos pares:", soma)
else:
    print("Número inválido.")
