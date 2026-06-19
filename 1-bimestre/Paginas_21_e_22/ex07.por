programa
{
    funcao inicio()
    {
        caracter letra

        escreva("Digite uma letra: ")
        leia(letra)

        se (letra == 'a' ou letra == 'e' ou letra == 'i' ou letra == 'o' ou letra == 'u' ou
            letra == 'A' ou letra == 'E' ou letra == 'I' ou letra == 'O' ou letra == 'U')
        {
            escreva(letra, " é uma vogal.")
        }
        senao
        {
            escreva(letra, " não é uma vogal.")
        }
    }
}
