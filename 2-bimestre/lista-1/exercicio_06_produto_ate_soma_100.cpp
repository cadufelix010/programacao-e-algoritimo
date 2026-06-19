#include <iostream>
using namespace std;

int main() {
    double numero;
    double soma = 0;
    double produto = 1;

    cout << "Digite numeros ate que a soma ultrapasse 100." << endl;

    while (soma <= 100) {
        cout << "Numero: ";
        cin >> numero;

        soma += numero;
        produto *= numero;
    }

    cout << "Soma final: " << soma << endl;
    cout << "Multiplicacao dos numeros lidos: " << produto << endl;

    return 0;
}
