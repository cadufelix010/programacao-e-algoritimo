"""Sistema Lanchonete - 3º Bimestre - Turma A"""

produtos = [
    {"id": 1, "nome": "X-Burger", "preco": 15.00},
    {"id": 2, "nome": "X-Salada", "preco": 17.00},
    {"id": 3, "nome": "Batata Frita", "preco": 10.00},
    {"id": 4, "nome": "Refrigerante", "preco": 6.00},
]

vendas = []


def listar_produtos():
    """Lista os produtos cadastrados."""
    print("\n--- PRODUTOS ---")
    for produto in produtos:
        print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['preco']:.2f}")


def alterar_preco():
    """Turma A: altera o preço de um produto."""
    listar_produtos()
    try:
        produto_id = int(input("Digite o ID do produto: "))
        novo_preco = float(input("Digite o novo preço: R$ "))
    except ValueError:
        print("Digite valores válidos.")
        return

    if novo_preco < 0:
        print("O preço não pode ser negativo.")
        return

    for produto in produtos:
        if produto["id"] == produto_id:
            produto["preco"] = novo_preco
            print("Preço alterado com sucesso!")
            return
    print("Produto não encontrado.")


def remover_produto():
    """Turma A: remove um produto."""
    listar_produtos()
    try:
        produto_id = int(input("Digite o ID do produto: "))
    except ValueError:
        print("Digite um ID válido.")
        return

    for produto in produtos:
        if produto["id"] == produto_id:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            return
    print("Produto não encontrado.")


def pesquisar_produto():
    """Turma A: pesquisa produto pelo nome."""
    nome = input("Digite o nome do produto: ").strip().lower()
    encontrados = [p for p in produtos if nome in p["nome"].lower()]

    print("\n--- RESULTADO ---")
    if not encontrados:
        print("Nenhum produto encontrado.")
        return

    for produto in encontrados:
        print(f"ID: {produto['id']} | {produto['nome']} | R$ {produto['preco']:.2f}")


def registrar_venda():
    """Registra uma venda para o relatório da Turma A."""
    listar_produtos()
    try:
        produto_id = int(input("Digite o ID do produto vendido: "))
        quantidade = int(input("Digite a quantidade: "))
    except ValueError:
        print("Digite valores válidos.")
        return

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    for produto in produtos:
        if produto["id"] == produto_id:
            total = produto["preco"] * quantidade
            vendas.append({"produto": produto["nome"], "quantidade": quantidade, "total": total})
            print(f"Venda registrada: R$ {total:.2f}")
            return
    print("Produto não encontrado.")


def relatorio_vendas():
    """Turma A: mostra o relatório de vendas."""
    print("\n--- RELATÓRIO DE VENDAS ---")
    if not vendas:
        print("Nenhuma venda registrada.")
        return

    total = 0
    for venda in vendas:
        print(f"Produto: {venda['produto']} | Qtd: {venda['quantidade']} | Total: R$ {venda['total']:.2f}")
        total += venda["total"]
    print(f"TOTAL VENDIDO: R$ {total:.2f}")


def menu():
    while True:
        print("\n===== SISTEMA LANCHONETE - TURMA A =====")
        print("1 - Listar produtos")
        print("2 - Alterar preço")
        print("3 - Remover produto")
        print("4 - Pesquisar produto por nome")
        print("5 - Registrar venda")
        print("6 - Relatório de vendas")
        print("0 - Sair")

        opcao = input("Escolha: ")
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
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()
