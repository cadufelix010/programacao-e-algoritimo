#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "Digite um numero: ";
    cin >> n;

    if (n > 0)
        cout << "Positivo";
    else if (n < 0)
        cout << "Negativo";
    else
        cout << "Zero";

    return 0;
}
