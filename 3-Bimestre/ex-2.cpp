#include <iostream>
using namespace std;

int main() {
    int n1, n2;
    cout << "Digite o primeiro numero: ";
    cin >> n1;
    cout << "Digite o segundo numero: ";
    cin >> n2;

    if (n1 > n2)
        cout << n1 << " e maior";
    else if (n2 > n1)
        cout << n2 << " e maior";
    else
        cout << "Os numeros sao iguais";

    return 0;
}
