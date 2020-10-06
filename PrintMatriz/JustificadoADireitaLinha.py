#O primeiro argumento recebe uma lista e o segundo um inteiro com o tamanho que cada valor da lista vai ficar.
def JustificadoDireitaLinha(lista, t):
    final = ""
    for i in range(len(lista)):
        if i == 0:
            final += "%*s" %(t, str(lista[i]))
        else:
            final += "%*s" %(t+1, str(lista[i]))
    return final

#Exemplo
lista = ["arroz", "abacate", "feijao", "beterraba"]

print(JustificadoDireitaLinha(lista, 10))

#Saida esperada
#     arroz    abacate     feijao  beterraba