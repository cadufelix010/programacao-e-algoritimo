programa
{
    funcao inicio()
    {
        real tempo, preco

        escreva("Digite o tempo de permanência em horas: ")
        leia(tempo)

        se (tempo <= 0)
        {
            escreva("Tempo inválido.")
        }
        senao se (tempo <= 2)
        {
            preco = tempo * 2
            escreva("Valor a pagar: R$ ", preco)
        }
        senao
        {
            preco = 4 + (tempo - 2)
            escreva("Valor a pagar: R$ ", preco)
        }
    }
}
