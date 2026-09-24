"""
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 10 - Sistema simples de senha
"""

senha_correta = "1234"
tentativas = 0
acesso_liberado = False

while tentativas < 3:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        acesso_liberado = True
        break

    print("Senha incorreta.")
    tentativas += 1

if acesso_liberado:
    print("Acesso liberado.")
else:
    print("Acesso bloqueado.")
