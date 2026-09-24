/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 06 - Média de notas
*/
#include <iostream>
using namespace std;

int main() {
    float nota;
    float soma = 0;
    int quantidade = 0;

    cout << "Digite uma nota entre 0 e 10: ";
    cin >> nota;

    while (nota >= 0 && nota <= 10) {
        soma += nota;
        quantidade++;

        cout << "Digite outra nota ou um valor invalido para encerrar: ";
        cin >> nota;
    }

    if (quantidade > 0) {
        cout << "Media das notas: " << soma / quantidade << endl;
    } else {
        cout << "Nenhuma nota valida foi digitada." << endl;
    }

    return 0;
}
