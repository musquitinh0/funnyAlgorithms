#ifndef Velho_H
#define Velho_H

class Velho : public Imovel {  //indicação de herança
  public:
      Velho(string = "Rua Amauri- sales", int = 428); //enviando valores padrões.
      void porcentagemDesconto(float, int);
      void impressaoValor();
      void getEndereco();
};

#endif
