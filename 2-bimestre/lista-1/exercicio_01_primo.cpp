#include <iostream>
using namespace std;

int main() {
    int numero;
    bool primo = true;

    cout << "Digite um numero inteiro: ";
    cin >> numero;

    if (numero < 2) {
        primo = false;
    } else {
        for (int divisor = 2; divisor * divisor <= numero; divisor++) {
            if (numero % divisor == 0) {
                primo = false;
                break;
            }
        }
    }

    if (primo) {
        cout << numero << " e um numero primo." << endl;
    } else {
        cout << numero << " nao e um numero primo." << endl;
    }

    return 0;
}
