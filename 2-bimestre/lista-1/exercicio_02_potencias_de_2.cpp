#include <iostream>
using namespace std;

int main() {
    int numero;
    unsigned long long potencia = 1;

    cout << "Digite um numero inteiro nao negativo: ";
    cin >> numero;

    if (numero < 0) {
        cout << "O numero deve ser maior ou igual a zero." << endl;
        return 1;
    }

    for (int expoente = 0; expoente <= numero; expoente++) {
        cout << "2^" << expoente << " = " << potencia << endl;
        potencia *= 2;
    }

    return 0;
}
