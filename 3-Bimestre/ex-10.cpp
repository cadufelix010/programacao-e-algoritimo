#include <iostream>
using namespace std;

int main() {
    string senha;
    string senhaCorreta = "1234";
    int tentativas = 0;

    while (tentativas < 3) {
        cout << "Digite a senha: ";
        cin >> senha;

        if (senha == senhaCorreta) {
            cout << "Acesso permitido";
            break;
        } else {
            cout << "Senha incorreta" << endl;
            tentativas++;
        }
    }

    if (tentativas == 3)
        cout << "Acesso bloqueado";

    return 0;
}
