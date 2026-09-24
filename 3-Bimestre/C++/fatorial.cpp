/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 09 - Fatorial
*/
#include <iostream>
using namespace std;

int main() {
    int numero;
    int contador = 1;
    long long fatorial = 1;

    cout << "Digite um numero inteiro maior ou igual a zero: ";
    cin >> numero;

    if (numero < 0) {
        cout << "Numero invalido." << endl;
        return 0;
    }

    while (contador <= numero) {
        fatorial *= contador;
        contador++;
    }

    cout << "Fatorial: " << fatorial << endl;
    return 0;
}
