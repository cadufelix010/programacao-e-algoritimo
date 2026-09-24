/*
Aluno: Carlos Eduardo Félix
3º Bimestre
Exercício 10 - Sistema simples de senha
*/
#include <iostream>
using namespace std;

int main() {
    int senha;
    const int senhaCorreta = 1234;
    int tentativas = 0;

    while (tentativas < 3) {
        cout << "Digite a senha: ";
        cin >> senha;

        if (senha == senhaCorreta) {
            cout << "Acesso liberado." << endl;
            return 0;
        }

        tentativas++;
        cout << "Senha incorreta." << endl;
    }

    cout << "Acesso bloqueado." << endl;
    return 0;
}
