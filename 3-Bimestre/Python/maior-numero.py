"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 02 - Maior entre dois números
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os números são iguais.")
