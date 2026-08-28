#include <iostream>
using namespace std;

int main() {
    float nota, soma = 0, media;
    int contador = 0;

    cout << "Digite uma nota de 0 a 10: ";
    cin >> nota;

    while (nota >= 0 && nota <= 10) {
        soma = soma + nota;
        contador++;
        cout << "Digite outra nota ou um numero fora de 0 a 10 para parar: ";
        cin >> nota;
    }

    if (contador > 0) {
        media = soma / contador;
        cout << "Media: " << media;
    } else {
        cout << "Nenhuma nota valida";
    }

    return 0;
}
