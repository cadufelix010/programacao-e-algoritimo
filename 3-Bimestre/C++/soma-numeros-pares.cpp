/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 04 - Soma dos números pares
*/
#include <iostream>
using namespace std;

int main() {
    int numero;
    int contador = 1;
    int soma = 0;

    cout << "Digite um numero inteiro positivo: ";
    cin >> numero;

    if (numero <= 0) {
        cout << "Numero invalido." << endl;
        return 0;
    }

    while (contador <= numero) {
        if (contador % 2 == 0) {
            soma += contador;
        }
        contador++;
    }

    cout << "Soma dos pares: " << soma << endl;
    return 0;
}
