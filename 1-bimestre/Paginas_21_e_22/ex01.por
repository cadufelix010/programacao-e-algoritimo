programa
{
    funcao inicio()
    {
        inteiro ano

        escreva("Digite um ano: ")
        leia(ano)

        se ((ano % 4 == 0 e ano % 100 != 0) ou ano % 400 == 0)
        {
            escreva(ano, " é bissexto.")
        }
        senao
        {
            escreva(ano, " não é bissexto.")
        }
    }
}
