#include <iostream>
using namespace std;

int main() {
    double numero;
    double soma = 0;

    cout << "Digite numeros. Para encerrar, digite um numero negativo." << endl;

    while (true) {
        cout << "Numero: ";
        cin >> numero;

        if (numero < 0) {
            break;
        }

        soma += numero;
    }

    cout << "Soma dos numeros digitados: " << soma << endl;

    return 0;
}
