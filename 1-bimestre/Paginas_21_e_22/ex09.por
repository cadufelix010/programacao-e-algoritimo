programa
{
    inclua biblioteca Matematica

    funcao inicio()
    {
        real numero, raiz
        inteiro raiz_inteira

        escreva("Digite um número não negativo: ")
        leia(numero)

        se (numero < 0)
        {
            escreva("Número inválido.")
        }
        senao
        {
            raiz = Matematica.raiz(numero, 2)
            raiz_inteira = inteiro(raiz)

            se (raiz_inteira * raiz_inteira == numero)
            {
                escreva(numero, " é um quadrado perfeito.")
            }
            senao
            {
                escreva(numero, " não é um quadrado perfeito.")
            }
        }
    }
}
