/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 03 - Contagem de 1 até N
*/
#include <iostream>
using namespace std;

int main() {
    int numero;
    int contador = 1;

    cout << "Digite um numero inteiro positivo: ";
    cin >> numero;

    if (numero <= 0) {
        cout << "Numero invalido." << endl;
        return 0;
    }

    while (contador <= numero) {
        cout << contador << endl;
        contador++;
    }

    return 0;
}
