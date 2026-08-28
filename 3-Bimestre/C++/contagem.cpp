#include <iostream>
using namespace std;

int main() {
    int n, contador = 1;
    cout << "Digite um numero positivo: ";
    cin >> n;

    if (n > 0) {
        while (contador <= n) {
            cout << contador << endl;
            contador++;
        }
    } else {
        cout << "Numero invalido";
    }

    return 0;
}
