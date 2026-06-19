programa
{
    funcao inicio()
    {
        real base_menor, base_maior, altura, area

        escreva("Digite a base menor: ")
        leia(base_menor)

        escreva("Digite a base maior: ")
        leia(base_maior)

        escreva("Digite a altura: ")
        leia(altura)

        area = (base_menor + base_maior) * altura / 2

        escreva("\nBase menor: ", base_menor)
        escreva("\nBase maior: ", base_maior)
        escreva("\nAltura: ", altura)
        escreva("\nÁrea do trapézio: ", area)
    }
}
