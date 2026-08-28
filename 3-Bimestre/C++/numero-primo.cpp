#include <iostream>
using namespace std;

int main() {
    int n, divisor = 1, quantidade = 0;
    cout << "Digite um numero positivo: ";
    cin >> n;

    if (n > 0) {
        while (divisor <= n) {
            if (n % divisor == 0)
                quantidade++;
            divisor++;
        }

        if (quantidade == 2)
            cout << "E primo";
        else
            cout << "Nao e primo";
    } else {
        cout << "Numero invalido";
    }

    return 0;
}
