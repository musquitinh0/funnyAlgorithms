#include "PesquisaDeDados.h"

int PesquisaDeDados::pesquisaLinear(string letra){
    cout << endl << "PESQUISA DE DADOS LINEAR" << endl;
      for (int i = 0; i < 25; i++){
        quantIteracoesLinear++;
        if (vetorLetras[i] == letra){
            cout << endl << "Quantidade de interações até chegar a letra " << letra << " foi: " << quantIteracoesLinear << endl;
        }
    }
    return 0;
}

int PesquisaDeDados::pesquisaBinaria(string letra){
    cout << endl << endl << "PESQUISA DE DADOS BINÁRIA" << endl;

    while (inicio <= fim){
        cout << endl << "O início, no momento, é: " << inicio << " e o final, no momento, é: " << fim << " enquanto o meio é: " << meio << endl;
        quantIteracoesBinaria++;
        if (letra == vetorLetras[meio]){
            cout << endl << "Achamos a letra " << vetorLetras[meio] << " depois de um total de " << quantIteracoesBinaria << " iterações" << endl;
            return 0;
        }

        else{
            if (letra < vetorLetras[meio]){
                fim = meio -1;
            }
            else{
                inicio = meio +1;
            }

        meio = (inicio + fim) / 2;

        }
    }
}
