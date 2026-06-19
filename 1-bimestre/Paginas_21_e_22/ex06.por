programa
{
    funcao inicio()
    {
        inteiro idade

        escreva("Digite a idade do passageiro: ")
        leia(idade)

        se (idade < 0)
        {
            escreva("Idade inválida.")
        }
        senao se (idade <= 2)
        {
            escreva("Tarifa gratuita.")
        }
        senao se (idade <= 12)
        {
            escreva("Meia tarifa.")
        }
        senao
        {
            escreva("Tarifa completa.")
        }
    }
}
