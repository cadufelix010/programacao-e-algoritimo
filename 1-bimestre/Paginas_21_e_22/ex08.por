programa
{
    funcao inicio()
    {
        inteiro n1, n2, n3, maior

        escreva("Digite o primeiro número: ")
        leia(n1)

        escreva("Digite o segundo número: ")
        leia(n2)

        escreva("Digite o terceiro número: ")
        leia(n3)

        maior = n1

        se (n2 > maior)
        {
            maior = n2
        }

        se (n3 > maior)
        {
            maior = n3
        }

        escreva("Maior valor: ", maior)
    }
}
