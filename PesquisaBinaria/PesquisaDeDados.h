//cabeçalho classe mãe
#ifndef PesquisaDeDados_H
#define PesquisaDeDados_H

class PesquisaDeDados{
	private: //atributos protegidos
		int quantIteracoesLinear = 0;
		int quantIteracoesBinaria = 0;
		int inicio = 0;
		int fim = 26;
		int meio = (inicio + fim)/2;
		string letraSelecionada;
		string vetorLetras[26] = {"A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};

    public:

        int pesquisaLinear(string);
        int pesquisaBinaria(string);
};

#endif
