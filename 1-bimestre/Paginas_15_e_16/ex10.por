programa
{
    funcao inicio()
    {
        inteiro qtd_1, qtd_5, qtd_10, qtd_25, qtd_50, qtd_100
        real valor_1, valor_5, valor_10, valor_25, valor_50, valor_100, total

        escreva("Quantidade de moedas de 1 centavo: ")
        leia(qtd_1)

        escreva("Quantidade de moedas de 5 centavos: ")
        leia(qtd_5)

        escreva("Quantidade de moedas de 10 centavos: ")
        leia(qtd_10)

        escreva("Quantidade de moedas de 25 centavos: ")
        leia(qtd_25)

        escreva("Quantidade de moedas de 50 centavos: ")
        leia(qtd_50)

        escreva("Quantidade de moedas de 1 real: ")
        leia(qtd_100)

        valor_1 = qtd_1 * 0.01
        valor_5 = qtd_5 * 0.05
        valor_10 = qtd_10 * 0.10
        valor_25 = qtd_25 * 0.25
        valor_50 = qtd_50 * 0.50
        valor_100 = qtd_100 * 1.00

        total = valor_1 + valor_5 + valor_10 + valor_25 + valor_50 + valor_100

        escreva("\nValor em moedas de 1 centavo: R$ ", valor_1)
        escreva("\nValor em moedas de 5 centavos: R$ ", valor_5)
        escreva("\nValor em moedas de 10 centavos: R$ ", valor_10)
        escreva("\nValor em moedas de 25 centavos: R$ ", valor_25)
        escreva("\nValor em moedas de 50 centavos: R$ ", valor_50)
        escreva("\nValor em moedas de 1 real: R$ ", valor_100)
        escreva("\nTotal recebido: R$ ", total)
    }
}
