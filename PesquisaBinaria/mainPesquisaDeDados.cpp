#include <iostream>
#include <locale>
#include <ctime>

using namespace std;

#include "PesquisaDeDados.cpp"

int main(){

setlocale(LC_ALL,"portuguese");

    PesquisaDeDados p1;
    string letra;

    cout << "Qual letra você deseja procurar no alfabeto? Por favor, digite em maiúsculo para procurarmos em nosso dicionário! (:";
    cin >> letra;

    p1.pesquisaLinear(letra);

    p1.pesquisaBinaria(letra);


return 0;
}
