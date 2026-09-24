/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 08 - Número primo
*/
#include <iostream>
using namespace std;

int main() {
    int numero;
    int divisor = 1;
    int quantidadeDivisores = 0;

    cout << "Digite um numero inteiro positivo: ";
    cin >> numero;

    if (numero <= 0) {
        cout << "Numero invalido." << endl;
        return 0;
    }

    while (divisor <= numero) {
        if (numero % divisor == 0) {
            quantidadeDivisores++;
        }
        divisor++;
    }

    if (quantidadeDivisores == 2) {
        cout << "O numero e primo." << endl;
    } else {
        cout << "O numero nao e primo." << endl;
    }

    return 0;
}
