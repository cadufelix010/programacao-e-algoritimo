#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    int quantidade;
    double altura;
    double somaAlturas = 0;

    cout << "Digite a quantidade de pessoas: ";
    cin >> quantidade;

    if (quantidade <= 0) {
        cout << "A quantidade de pessoas deve ser maior que zero." << endl;
        return 1;
    }

    for (int i = 1; i <= quantidade; i++) {
        cout << "Digite a altura da pessoa " << i << " em metros: ";
        cin >> altura;

        if (altura <= 0) {
            cout << "Altura invalida." << endl;
            return 1;
        }

        somaAlturas += altura;
    }

    double media = somaAlturas / quantidade;

    cout << fixed << setprecision(2);
    cout << "Altura media: " << media << " m" << endl;

    return 0;
}
