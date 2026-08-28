#include <iostream>
using namespace std;

int main() {
    int n, contador = 1, fatorial = 1;
    cout << "Digite um numero: ";
    cin >> n;

    if (n >= 0) {
        while (contador <= n) {
            fatorial = fatorial * contador;
            contador++;
        }
        cout << "Fatorial: " << fatorial;
    } else {
        cout << "Numero invalido";
    }

    return 0;
}
