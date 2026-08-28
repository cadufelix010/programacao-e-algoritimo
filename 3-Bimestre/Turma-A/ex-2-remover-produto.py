produtos = [
    {"id": 1, "nome": "X-Burger", "preco": 15.00},
    {"id": 2, "nome": "X-Salada", "preco": 17.00},
    {"id": 3, "nome": "Batata Frita", "preco": 10.00}
]

print('--- PRODUTOS ---')
for produto in produtos:
    print(f"{produto['id']} - {produto['nome']} - R$ {produto['preco']:.2f}")

idproduto = int(input('Digite o ID do produto que deseja remover: '))

produtoencontrado = False

for produto in produtos:
    if produto['id'] == idproduto:
        produtos.remove(produto)
        produtoencontrado = True
        print('Produto removido com sucesso!')
        break

if not produtoencontrado:
    print('Produto não encontrado.')

print('\n--- PRODUTOS ATUALIZADOS ---')
for produto in produtos:
    print(f"{produto['id']} - {produto['nome']} - R$ {produto['preco']:.2f}")
