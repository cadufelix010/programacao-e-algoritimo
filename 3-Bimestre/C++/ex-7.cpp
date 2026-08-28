#include <iostream>
using namespace std;

int main() {
    int n, contador = 1;
    int positivos = 0, negativos = 0, zeros = 0;

    while (contador <= 10) {
        cout << "Digite um numero: ";
        cin >> n;

        if (n > 0)
            positivos++;
        else if (n < 0)
            negativos++;
        else
            zeros++;

        contador++;
    }

    cout << "Positivos: " << positivos << endl;
    cout << "Negativos: " << negativos << endl;
    cout << "Zeros: " << zeros;

    return 0;
}
