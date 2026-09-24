"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 06 - Média de notas
"""

soma = 0
quantidade = 0

nota = float(input("Digite uma nota entre 0 e 10: "))

while 0 <= nota <= 10:
    soma += nota
    quantidade += 1
    nota = float(
        input("Digite outra nota ou um valor inválido para encerrar: ")
    )

if quantidade > 0:
    print("Média das notas:", soma / quantidade)
else:
    print("Nenhuma nota válida foi digitada.")
