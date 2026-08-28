vendas = [
    {"produto": "X-Burger", "quantidade": 2, "total": 30.00},
    {"produto": "X-Salada", "quantidade": 1, "total": 17.00},
    {"produto": "Refrigerante", "quantidade": 3, "total": 18.00}
]

totalvendido = 0

print('--- RELATÓRIO DE VENDAS ---')

for venda in vendas:
    print(f"Produto: {venda['produto']} | Quantidade: {venda['quantidade']} | Total: R$ {venda['total']:.2f}")
    totalvendido += venda['total']

print(f'\nTotal vendido: R$ {totalvendido:.2f}')
