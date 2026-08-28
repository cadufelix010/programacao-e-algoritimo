produtos = [
    {"id": 1, "nome": "X-Burger", "preco": 15.00},
    {"id": 2, "nome": "X-Salada", "preco": 17.00},
    {"id": 3, "nome": "Batata Frita", "preco": 10.00}
]

print('--- PRODUTOS ---')
for produto in produtos:
    print(f"{produto['id']} - {produto['nome']} - R$ {produto['preco']:.2f}")

idproduto = int(input('Digite o ID do produto: '))
novopreco = float(input('Digite o novo preço: R$ '))

produtoencontrado = False

for produto in produtos:
    if produto['id'] == idproduto:
        produto['preco'] = novopreco
        produtoencontrado = True
        print('Preço alterado com sucesso!')
        print(f"{produto['nome']} - R$ {produto['preco']:.2f}")

if not produtoencontrado:
    print('Produto não encontrado.')
