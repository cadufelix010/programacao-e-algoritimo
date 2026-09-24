/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 02 - Maior entre dois números
*/
#include <iostream>
using namespace std;

int main() {
    int numero1, numero2;

    cout << "Digite o primeiro numero: ";
    cin >> numero1;

    cout << "Digite o segundo numero: ";
    cin >> numero2;

    if (numero1 > numero2) {
        cout << "O maior numero e: " << numero1 << endl;
    } else if (numero2 > numero1) {
        cout << "O maior numero e: " << numero2 << endl;
    } else {
        cout << "Os numeros sao iguais." << endl;
    }

    return 0;
}
