programa
{
    funcao inicio()
    {
        real peso_atual, percentual_engorda, aumento, novo_peso

        escreva("Digite o peso atual do boi: ")
        leia(peso_atual)

        escreva("Digite o percentual de engorda: ")
        leia(percentual_engorda)

        aumento = peso_atual * percentual_engorda / 100
        novo_peso = peso_atual + aumento

        escreva("\nPeso atual: ", peso_atual, " kg")
        escreva("\nPercentual de engorda: ", percentual_engorda, "%")
        escreva("\nNovo peso: ", novo_peso, " kg")
    }
}
