programa
{
    funcao inicio()
    {
        inteiro classificacao

        escreva("Digite a classificação indicativa: ")
        leia(classificacao)

        se (classificacao < 0)
        {
            escreva("Classificação inválida.")
        }
        senao se (classificacao <= 10)
        {
            escreva("Categoria infantil.")
        }
        senao se (classificacao <= 14)
        {
            escreva("Categoria infantojuvenil.")
        }
        senao se (classificacao <= 17)
        {
            escreva("Categoria juvenil.")
        }
        senao
        {
            escreva("Categoria adulto.")
        }
    }
}
