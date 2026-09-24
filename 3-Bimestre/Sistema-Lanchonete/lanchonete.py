"""
Sistema Lanchonete - 3º Bimestre
Aluno: Carlos Eduardo Félix
Turma A

Funcionalidades principais:
1 - Cadastrar produto
2 - Listar produtos
3 - Fazer pedido
4 - Ver pedidos
5 - Alterar preço
6 - Remover produto
7 - Pesquisar produto por nome
8 - Relatório de vendas
9 - Sair
"""

import json
import os

DATA_FILE = "lanchonete_dados.json"

products = []
orders = []


def load_data():
    global products, orders

    if not os.path.exists(DATA_FILE):
        products = []
        orders = []
        save_data()
        return

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            products = data.get("products", [])
            orders = data.get("orders", [])
    except (json.JSONDecodeError, OSError):
        products = []
        orders = []
        save_data()


def save_data():
    data = {
        "products": products,
        "orders": orders
    }

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def read_float(message):
    while True:
        try:
            return float(input(message).replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número.")


def read_int(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Valor inválido. Digite um número inteiro.")


def find_product_by_code(code):
    for product in products:
        if product["code"] == code:
            return product
    return None


def register_product():
    print("\n--- CADASTRAR PRODUTO ---")
    code = input("Código do produto: ").strip()

    if not code:
        print("Código inválido.")
        return

    if find_product_by_code(code) is not None:
        print("Já existe um produto com este código.")
        return

    name = input("Nome do produto: ").strip()
    price = read_float("Preço do produto: R$ ")
    stock = read_int("Quantidade em estoque: ")

    if not name or price < 0 or stock < 0:
        print("Dados inválidos.")
        return

    products.append({
        "code": code,
        "name": name,
        "price": price,
        "stock": stock
    })

    save_data()
    print("Produto cadastrado com sucesso!")


def list_products():
    print("\n--- PRODUTOS CADASTRADOS ---")

    if not products:
        print("Nenhum produto cadastrado.")
        return

    for product in products:
        print(
            f"Código: {product['code']} | "
            f"Nome: {product['name']} | "
            f"Preço: R$ {product['price']:.2f} | "
            f"Estoque: {product['stock']}"
        )


def make_order():
    print("\n--- FAZER PEDIDO ---")

    if not products:
        print("Nenhum produto cadastrado.")
        return

    customer_name = input("Nome do cliente: ").strip()
    list_products()

    code = input("Código do produto: ").strip()
    product = find_product_by_code(code)

    if product is None:
        print("Produto não encontrado.")
        return

    quantity = read_int("Quantidade desejada: ")

    if quantity <= 0:
        print("Quantidade inválida.")
        return

    if quantity > product["stock"]:
        print("Estoque insuficiente.")
        return

    total = quantity * product["price"]
    product["stock"] -= quantity

    orders.append({
        "customer_name": customer_name,
        "product_code": product["code"],
        "product_name": product["name"],
        "quantity": quantity,
        "unit_price": product["price"],
        "total": total
    })

    save_data()
    print(f"Pedido realizado com sucesso! Total: R$ {total:.2f}")


def list_orders():
    print("\n--- PEDIDOS REALIZADOS ---")

    if not orders:
        print("Nenhum pedido realizado.")
        return

    for number, order in enumerate(orders, start=1):
        print(
            f"{number}. Cliente: {order['customer_name']} | "
            f"Produto: {order['product_name']} | "
            f"Qtd: {order['quantity']} | "
            f"Total: R$ {order['total']:.2f}"
        )


def change_product_price():
    print("\n--- ALTERAR PREÇO ---")
    code = input("Código do produto: ").strip()
    product = find_product_by_code(code)

    if product is None:
        print("Produto não encontrado.")
        return

    print(f"Produto: {product['name']}")
    print(f"Preço atual: R$ {product['price']:.2f}")

    new_price = read_float("Novo preço: R$ ")

    if new_price < 0:
        print("O preço não pode ser negativo.")
        return

    product["price"] = new_price
    save_data()
    print("Preço alterado com sucesso!")


def remove_product():
    print("\n--- REMOVER PRODUTO ---")
    code = input("Código do produto: ").strip()
    product = find_product_by_code(code)

    if product is None:
        print("Produto não encontrado.")
        return

    confirmation = input(
        f"Remover '{product['name']}'? (s/n): "
    ).strip().lower()

    if confirmation == "s":
        products.remove(product)
        save_data()
        print("Produto removido com sucesso!")
    else:
        print("Operação cancelada.")


def search_product_by_name():
    print("\n--- PESQUISAR PRODUTO ---")
    search = input("Digite o nome ou parte do nome: ").strip().lower()

    if not search:
        print("Pesquisa inválida.")
        return

    found = [
        product for product in products
        if search in product["name"].lower()
    ]

    if not found:
        print("Nenhum produto encontrado.")
        return

    for product in found:
        print(
            f"Código: {product['code']} | "
            f"Nome: {product['name']} | "
            f"Preço: R$ {product['price']:.2f} | "
            f"Estoque: {product['stock']}"
        )


def sales_report():
    print("\n--- RELATÓRIO DE VENDAS ---")

    if not orders:
        print("Nenhuma venda registrada.")
        return

    total_sales = sum(order["total"] for order in orders)
    total_items = sum(order["quantity"] for order in orders)

    print(f"Quantidade de pedidos: {len(orders)}")
    print(f"Quantidade de itens vendidos: {total_items}")
    print(f"Valor total vendido: R$ {total_sales:.2f}")
    print("\nVendas:")

    for number, order in enumerate(orders, start=1):
        print(
            f"{number}. {order['product_name']} - "
            f"{order['quantity']} un. - "
            f"R$ {order['total']:.2f}"
        )


def show_menu():
    print("\n=== SISTEMA LANCHONETE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Fazer pedido")
    print("4 - Ver pedidos realizados")
    print("5 - Alterar preço de produto")
    print("6 - Remover produto")
    print("7 - Pesquisar produto por nome")
    print("8 - Relatório de vendas")
    print("9 - Sair")


def main():
    load_data()

    while True:
        show_menu()
        option = input("Escolha uma opção: ").strip()

        if option == "1":
            register_product()
        elif option == "2":
            list_products()
        elif option == "3":
            make_order()
        elif option == "4":
            list_orders()
        elif option == "5":
            change_product_price()
        elif option == "6":
            remove_product()
        elif option == "7":
            search_product_by_name()
        elif option == "8":
            sales_report()
        elif option == "9":
            save_data()
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
