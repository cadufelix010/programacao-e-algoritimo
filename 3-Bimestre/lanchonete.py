"""
Sistema Lanchonete - 3º Bimestre
Programação e Algoritmo

Turma A:
- Alterar preço de produto
- Remover produto
- Pesquisar produto por nome
- Relatório de vendas

Sistema simples, feito apenas com recursos básicos do Python,
para facilitar o estudo e os testes em sala de aula.
"""

from datetime import datetime


# Lista de produtos cadastrados
produtos = [
    {"id": 1, "nome": "X-Burger", "preco": 15.00},
    {"id": 2, "nome": "X-Salada", "preco": 17.00},
    {"id": 3, "nome": "Batata Frita", "preco": 10.00},
    {"id": 4, "nome": "Refrigerante", "preco": 6.00},
]

# Lista de vendas realizadas
vendas = []


def listar_produtos():
    """Exibe todos os produtos cadastrados."""
    print("\n--- PRODUTOS ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['preco']:.2f}")


def alterar_preco():
    """Altera o preço de um produto pelo ID."""
    listar_produtos()

    try:
        produto_id = int(input("Digite o ID do produto: "))
        novo_preco = float(input("Digite o novo preço: R$ "))
    except ValueError:
        print("Erro: digite valores válidos.")
        return

    if novo_preco < 0:
        print("Erro: o preço não pode ser negativo.")
        return

    for produto in produtos:
        if produto["id"] == produto_id:
            produto["preco"] = novo_preco
            print(f"Preço de '{produto['nome']}' alterado com sucesso!")
            return

    print("Produto não encontrado.")


def remover_produto():
    """Remove um produto pelo ID."""
    listar_produtos()

    try:
        produto_id = int(input("Digite o ID do produto que deseja remover: "))
    except ValueError:
        print("Erro: digite um ID válido.")
        return

    for produto in produtos:
        if produto["id"] == produto_id:
            produtos.remove(produto)
            print(f"Produto '{produto['nome']}' removido com sucesso!")
            return

    print("Produto não encontrado.")


def pesquisar_produto():
    """Pesquisa produtos pelo nome, aceitando parte do nome."""
    nome = input("Digite o nome do produto para pesquisar: ").strip().lower()

    if not nome:
        print("Digite um nome para realizar a pesquisa.")
        return

    encontrados = [
        produto for produto in produtos
        if nome in produto["nome"].lower()
    ]

    print("\n--- RESULTADO DA PESQUISA ---")
    if not encontrados:
        print("Nenhum produto encontrado.")
        return

    for produto in encontrados:
        print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['preco']:.2f}")


def registrar_venda():
    """Registra uma venda simples para permitir o relatório de vendas."""
    listar_produtos()

    try:
        produto_id = int(input("Digite o ID do produto vendido: "))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Erro: digite valores válidos.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    for produto in produtos:
        if produto["id"] == produto_id:
            total = produto["preco"] * quantidade
            vendas.append({
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                "produto": produto["nome"],
                "quantidade": quantidade,
                "preco_unitario": produto["preco"],
                "total": total,
            })
            print(f"Venda registrada! Total: R$ {total:.2f}")
            return

    print("Produto não encontrado.")


def relatorio_vendas():
    """Exibe o relatório de todas as vendas registradas."""
    print("\n--- RELATÓRIO DE VENDAS ---")

    if not vendas:
        print("Nenhuma venda registrada.")
        return

    total_vendido = 0

    for venda in vendas:
        print(
            f"Data: {venda['data']} | "
            f"Produto: {venda['produto']} | "
            f"Qtd: {venda['quantidade']} | "
            f"Total: R$ {venda['total']:.2f}"
        )
        total_vendido += venda["total"]

    print(f"\nTOTAL VENDIDO: R$ {total_vendido:.2f}")


def menu():
    """Menu principal do Sistema Lanchonete."""
    while True:
        print("\n==============================")
        print("       SISTEMA LANCHONETE")
        print("       3º BIMESTRE")
        print("==============================")
        print("1 - Listar produtos")
        print("2 - Alterar preço de produto")
        print("3 - Remover produto")
        print("4 - Pesquisar produto por nome")
        print("5 - Registrar venda")
        print("6 - Relatório de vendas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            alterar_preco()
        elif opcao == "3":
            remover_produto()
        elif opcao == "4":
            pesquisar_produto()
        elif opcao == "5":
            registrar_venda()
        elif opcao == "6":
            relatorio_vendas()
        elif opcao == "0":
            print("Sistema encerrado. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
