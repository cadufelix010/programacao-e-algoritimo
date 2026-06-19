programa
{
    funcao inicio()
    {
        real valor, desconto, valor_final

        escreva("Digite o valor da compra: R$ ")
        leia(valor)

        se (valor < 100)
        {
            desconto = 0
        }
        senao se (valor <= 500)
        {
            desconto = valor * 10 / 100
        }
        senao
        {
            desconto = valor * 20 / 100
        }

        valor_final = valor - desconto

        escreva("\nValor da compra: R$ ", valor)
        escreva("\nDesconto: R$ ", desconto)
        escreva("\nValor final: R$ ", valor_final)
    }
}
