#include <iostream>
using namespace std;

int main() {
    int numeroFinal;
    long long somaPares = 0;
    long long somaImpares = 0;

    cout << "Digite um numero inteiro nao negativo: ";
    cin >> numeroFinal;

    if (numeroFinal < 0) {
        cout << "O numero deve ser maior ou igual a zero." << endl;
        return 1;
    }

    for (int numero = 0; numero <= numeroFinal; numero++) {
        if (numero % 2 == 0) {
            somaPares += numero;
        } else {
            somaImpares += numero;
        }
    }

    cout << "Soma dos numeros pares: " << somaPares << endl;
    cout << "Soma dos numeros impares: " << somaImpares << endl;

    return 0;
}
