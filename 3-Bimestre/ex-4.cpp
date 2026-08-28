#include <iostream>
using namespace std;

int main() {
    int n, contador = 1, soma = 0;
    cout << "Digite um numero positivo: ";
    cin >> n;

    if (n > 0) {
        while (contador <= n) {
            if (contador % 2 == 0)
                soma = soma + contador;
            contador++;
        }
        cout << "Soma dos numeros pares: " << soma;
    } else {
        cout << "Numero invalido";
    }

    return 0;
}
