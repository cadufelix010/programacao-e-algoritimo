programa
{
    funcao inicio()
    {
        real preco_litro, valor_abastecimento, litros

        escreva("Digite o preço do litro do combustível: ")
        leia(preco_litro)

        escreva("Digite o valor que deseja abastecer: ")
        leia(valor_abastecimento)

        se (preco_litro <= 0)
        {
            escreva("Preço do litro inválido.")
        }
        senao
        {
            litros = valor_abastecimento / preco_litro

            escreva("\nPreço do litro: R$ ", preco_litro)
            escreva("\nValor do abastecimento: R$ ", valor_abastecimento)
            escreva("\nQuantidade de litros: ", litros)
        }
    }
}
