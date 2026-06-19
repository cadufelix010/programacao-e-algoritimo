programa
{
    funcao inicio()
    {
        cadeia nome
        inteiro idade_anos, idade_meses, idade_dias

        escreva("Digite o nome: ")
        leia(nome)

        escreva("Digite a idade em anos: ")
        leia(idade_anos)

        idade_meses = idade_anos * 12
        idade_dias = idade_anos * 365

        escreva("\nNome: ", nome)
        escreva("\nIdade em anos: ", idade_anos)
        escreva("\nIdade em meses: ", idade_meses)
        escreva("\nIdade em dias: ", idade_dias)
    }
}
