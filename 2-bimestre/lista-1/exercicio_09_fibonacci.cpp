#include <iostream>
using namespace std;

int main() {
    int limite;

    cout << "Digite um numero entre 50 e 100: ";
    cin >> limite;

    if (limite < 50 || limite > 100) {
        cout << "Valor invalido. Digite um numero entre 50 e 100." << endl;
        return 1;
    }

    int anterior = 0;
    int atual = 1;

    cout << "Sequencia de Fibonacci ate " << limite << ":" << endl;
    cout << anterior << " ";

    while (atual <= limite) {
        cout << atual << " ";

        int proximo = anterior + atual;
        anterior = atual;
        atual = proximo;
    }

    cout << endl;

    return 0;
}
