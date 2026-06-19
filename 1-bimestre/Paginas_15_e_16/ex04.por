programa
{
    funcao inicio()
    {
        real nota1, nota2, nota3, nota4, media

        escreva("Digite a primeira nota: ")
        leia(nota1)

        escreva("Digite a segunda nota: ")
        leia(nota2)

        escreva("Digite a terceira nota: ")
        leia(nota3)

        escreva("Digite a quarta nota: ")
        leia(nota4)

        media = (nota1 * 1 + nota2 * 2 + nota3 * 3 + nota4 * 4) / 10

        escreva("\nNota 1: ", nota1)
        escreva("\nNota 2: ", nota2)
        escreva("\nNota 3: ", nota3)
        escreva("\nNota 4: ", nota4)
        escreva("\nMédia ponderada: ", media)
    }
}
