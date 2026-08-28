senha_correta = '1234'
attempts = 0

while attempts < 3:
    senha = input('Digite a senha: ')
    if senha == senha_correta:
        print('Acesso permitido')
        break
    else:
        attempts += 1
        print('Senha incorreta')

if attempts == 3:
    print('Acesso bloqueado')
