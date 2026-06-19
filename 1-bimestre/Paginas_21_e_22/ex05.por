programa
{
    funcao inicio()
    {
        real etanol, gasolina, limite

        escreva("Digite o preço do etanol: R$ ")
        leia(etanol)

        escreva("Digite o preço da gasolina: R$ ")
        leia(gasolina)

        limite = gasolina * 70 / 100

        se (etanol <= limite)
        {
            escreva("Abastecer com etanol.")
        }
        senao
        {
            escreva("Abastecer com gasolina.")
        }
    }
}
