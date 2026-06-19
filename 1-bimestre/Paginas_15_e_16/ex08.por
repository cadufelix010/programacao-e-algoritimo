programa
{
    funcao inicio()
    {
        real salario_fixo, vendas, percentual, comissao, salario_final

        escreva("Digite o salário fixo: ")
        leia(salario_fixo)

        escreva("Digite o valor total das vendas: ")
        leia(vendas)

        escreva("Digite o percentual de comissão: ")
        leia(percentual)

        comissao = vendas * percentual / 100
        salario_final = salario_fixo + comissao

        escreva("\nSalário fixo: R$ ", salario_fixo)
        escreva("\nValor das vendas: R$ ", vendas)
        escreva("\nPercentual de comissão: ", percentual, "%")
        escreva("\nValor da comissão: R$ ", comissao)
        escreva("\nSalário final: R$ ", salario_final)
    }
}
