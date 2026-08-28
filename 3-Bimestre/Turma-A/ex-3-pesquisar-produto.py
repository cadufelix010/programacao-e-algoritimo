produtos = [
    {"id": 1, "nome": "X-Burger", "preco": 15.00},
    {"id": 2, "nome": "X-Salada", "preco": 17.00},
    {"id": 3, "nome": "Batata Frita", "preco": 10.00},
    {"id": 4, "nome": "Refrigerante", "preco": 6.00}
]

nome = input('Digite o nome do produto: ').lower()

produtoencontrado = False

for produto in produtos:
    if nome in produto['nome'].lower():
        print(f"ID: {produto['id']} - {produto['nome']} - R$ {produto['preco']:.2f}")
        produtoencontrado = True

if not produtoencontrado:
    print('Produto não encontrado.')
