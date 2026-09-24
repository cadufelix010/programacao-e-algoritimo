"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 05 - Tabuada com validação
"""

numero = int(input("Digite um número de 1 a 10: "))

while numero < 1 or numero > 10:
    numero = int(input("Valor inválido. Digite novamente: "))

contador = 1

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador += 1
