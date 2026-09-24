"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 03 - Contagem de 1 até N
"""

numero = int(input("Digite um número inteiro positivo: "))
contador = 1

if numero > 0:
    while contador <= numero:
        print(contador)
        contador += 1
else:
    print("Número inválido.")
