#O primeiro argumento recebe uma lista e o segundo um inteiro com o tamanho que cada valor da lista vai ficar.
def JustificadoDireitaLinha(lista, t):
    final = ""
    for i in range(len(lista)):
        if i == 0:
            final += "%*s" %(t, str(lista[i]))
        else:
            final += "%*s" %(t+1, str(lista[i]))
    return final

def JustificadoDireitaMatriz(lista, t):
    final = ""
    for i in range(len(lista)):
        if (i != len(lista)-1):
            final += JustificadoDireitaLinha(lista[i], t)+"\n"
        else:
            final += JustificadoDireitaLinha(lista[i], t)
    return final


# Exemplo
matriz = [
    ["arroz", "abacate"],
    ["feijao", "beterraba"]
]
print(JustificadoDireitaMatriz(matriz, 10))

# Saida esperada do exemplo
#     arroz    abacate
#    feijao  beterraba