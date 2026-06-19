#include <iostream>
using namespace std;

int main() {
    double numero;
    double menor, maior;

    cout << "Digite o 1o numero: ";
    cin >> numero;

    menor = numero;
    maior = numero;

    for (int i = 2; i <= 10; i++) {
        cout << "Digite o " << i << "o numero: ";
        cin >> numero;

        if (numero < menor) {
            menor = numero;
        }

        if (numero > maior) {
            maior = numero;
        }
    }

    cout << "Menor numero: " << menor << endl;
    cout << "Maior numero: " << maior << endl;

    return 0;
}
