senha_correta = 6777
tentativas = 1
limite = 5

senha = int(input('Digite a senha de 4 números: '))

while senha != senha_correta and tentativas < limite:
    print('Senha incorreta, tente novamente.\n')
    senha = int(input('Digite a senha de 4 números: '))
    tentativas += 1

if senha == senha_correta:
    print('Acesso liberado')
else:
    print('Acesso negado')
