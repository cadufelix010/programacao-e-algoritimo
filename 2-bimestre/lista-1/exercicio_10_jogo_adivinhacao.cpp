#include <iostream>
#include <random>
using namespace std;

int main() {
    random_device dispositivo;
    mt19937 gerador(dispositivo());
    uniform_int_distribution<int> distribuicao(1, 100);

    int numeroSecreto = distribuicao(gerador);
    int palpite;
    int tentativas = 0;

    cout << "Jogo de adivinhacao" << endl;
    cout << "Tente acertar um numero entre 1 e 100." << endl;

    do {
        cout << "Digite seu palpite: ";
        cin >> palpite;
        tentativas++;

        if (palpite < numeroSecreto) {
            cout << "Muito baixo." << endl;
        } else if (palpite > numeroSecreto) {
            cout << "Muito alto." << endl;
        } else {
            cout << "Correto!" << endl;
        }

    } while (palpite != numeroSecreto);

    cout << "Quantidade de palpites: " << tentativas << endl;

    return 0;
}
