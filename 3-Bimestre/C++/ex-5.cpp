#include <iostream>
using namespace std;

int main() {
    int n, contador = 1;
    cout << "Digite um numero de 1 a 10: ";
    cin >> n;

    if (n >= 1 && n <= 10) {
        while (contador <= 10) {
            cout << n << " x " << contador << " = " << n * contador << endl;
            contador++;
        }
    } else {
        cout << "Numero invalido";
    }

    return 0;
}
