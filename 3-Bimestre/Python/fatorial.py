"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 09 - Fatorial
"""

numero = int(input("Digite um número inteiro maior ou igual a zero: "))
contador = 1
fatorial = 1

if numero >= 0:
    while contador <= numero:
        fatorial *= contador
        contador += 1

    print("Fatorial:", fatorial)
else:
    print("Número inválido.")
