programa
{
    funcao inicio()
    {
        real a, b, c

        escreva("Digite o primeiro lado: ")
        leia(a)

        escreva("Digite o segundo lado: ")
        leia(b)

        escreva("Digite o terceiro lado: ")
        leia(c)

        se (a < b + c e b < a + c e c < a + b)
        {
            se (a == b e b == c)
            {
                escreva("Triângulo equilátero.")
            }
            senao se (a == b ou a == c ou b == c)
            {
                escreva("Triângulo isósceles.")
            }
            senao
            {
                escreva("Triângulo escaleno.")
            }
        }
        senao
        {
            escreva("Os valores não formam um triângulo.")
        }
    }
}
