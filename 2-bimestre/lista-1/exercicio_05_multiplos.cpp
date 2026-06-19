#include <iostream>
using namespace std;

int main() {
    int limite;
    int base;

    cout << "Digite o valor final do intervalo: ";
    cin >> limite;

    cout << "Digite o numero base dos multiplos: ";
    cin >> base;

    if (limite < 1) {
        cout << "O valor final deve ser maior ou igual a 1." << endl;
        return 1;
    }

    if (base == 0) {
        cout << "O numero base nao pode ser zero." << endl;
        return 1;
    }

    cout << "Multiplos de " << base << " entre 1 e " << limite << ":" << endl;

    bool encontrou = false;

    for (int numero = 1; numero <= limite; numero++) {
        if (numero % base == 0) {
            cout << numero << " ";
            encontrou = true;
        }
    }

    if (!encontrou) {
        cout << "Nenhum multiplo encontrado.";
    }

    cout << endl;

    return 0;
}
