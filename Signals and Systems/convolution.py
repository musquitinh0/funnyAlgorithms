#importando bibliotecas
import numpy as np
import matplotlib.pyplot as plt

#Funcao para realizar convolucao
def Conv(x,h,valor_inicial):
	#Inicializando algumas variaveis
	lenx = len(x)
	lenh = len(h)
	indep_values = np.arange(valor_inicial, valor_inicial+lenh+lenx-1,1)#Mantem o tamanho do vetor, independente do valor_inicial
	y = np.zeros(lenh+lenx-1)
	for i in range(lenh):
		for j in range(lenx):
			y[i+j] = y[i+j] + (h[i]*x[j]) #a medida em que os sinais vao se "interceptando", o valor de y se atualiza
	return (y, indep_values)

#Elaborando testes

#Os testes de 1 a 3 sao para verificar a funcionalidade do algoritmo 
#com as tres possibilidades de valor inicial

#Teste1 - Valor inicial negativo

x_teste1 = np.array([5,2,4,5,2,5,7,5])
h_teste1 = np.array([6,3,5,4,6])
(y_teste1,indep_values_teste1) = Conv(x_teste1,h_teste1,-4)
t_x_teste1 = np.arange(-4,-4+len(x_teste1),1)
t_h_teste1 = np.arange(-4,-4+len(h_teste1),1)

#Teste2 - Valor inicial positivo

x_teste2 = np.array([6,3,5,4,6])
h_teste2 = np.array([1,4,2])
(y_teste2,indep_values_teste2) = Conv(x_teste2,h_teste2,3)
t_x_teste2 = np.arange(3,3+len(x_teste2),1)
t_h_teste2 = np.arange(3,3+len(h_teste2),1)

#Teste3 - Valor inicial nulo
x_teste3 = np.array([1,1,-1,0,2,-2])
h_teste3 = np.array([-2,1,1,1,1])
(y_teste3,indep_values_teste3) = Conv(x_teste3,h_teste3,0)
t_x_teste3 = np.arange(len(x_teste3))
t_h_teste3 = np.arange(len(h_teste3))


#Os testes de 4 a 6 sao testes a fim de
#confirmar algumas das propriedades da convolucao

#Teste4 - Comutativa
#Comutando com o Teste2

x_teste4 = np.array([1,4,2])
h_teste4 = np.array([6,3,5,4,6])
(y_teste4,indep_values_teste4) = Conv(x_teste4,h_teste4,3)
t_x_teste4 = np.arange(3,3+len(x_teste4),1)
t_h_teste4 = np.arange(3,3+len(h_teste4),1)

#Teste5 - Distributiva
#Utilizando os testes 1 e 4
#Como o sistema eh LTI, os sinais podem ser convoluidos na origem,
#entao foram trocados os valores iniciais de todos os testes.

x_teste5 = np.array([6,6,6,5,2,5,7,5]) #Soma dos 'x_teste*' em questao
h_teste5 = np.array([6,3,5,4,6])
(y_teste5,indep_values_teste5) = Conv(x_teste5,h_teste5,0)
t_x_teste5 = np.arange(len(x_teste5))
t_h_teste5 = np.arange(len(h_teste5))

#Teste6 - Impulso como elemento neutro

x_teste6 = np.array([6,2,4,9,1])
h_teste6 = np.array([1])
(y_teste6,indep_values_teste6) = Conv(x_teste6,h_teste6,0)
t_x_teste6 = np.arange(len(x_teste6))
t_h_teste6 = np.arange(len(h_teste6))

#Plotando todos os graficos

#Teste1
plt.figure(1) #Cria a janela onde o grafico numero 1 sera mostrado

plt.subplot(3,1,1) #Area do primeiro grafico
plt.axis((-5,8,0,8))
plt.grid(True)
plt.plot(t_x_teste1, x_teste1, 'r*', label='x_teste1')
plt.xlabel('t')
plt.ylabel('x_teste1(t)')
plt.title('Teste1') #Nomear o primeiro grafico implica aqui em nomear o Teste por questao de estetica
plt.legend()

plt.subplot(3,1,2) #Area do segundo grafico
plt.axis((-5,8,0,8))
plt.grid(True)
plt.plot(t_h_teste1, h_teste1, 'gD', label='h_teste1')
plt.xlabel('t')
plt.ylabel('h_teste1(t)')
plt.legend()

plt.subplot(3,1,3) #Area do terceiro grafico
plt.axis((-5,8,20,120))
plt.grid(True)#Fica mais facil de identificar os pontos
plt.plot(indep_values_teste1, y_teste1, 'b^', label='y_teste1')
plt.xlabel('t')
plt.ylabel('y_teste1(t)')
plt.legend()

plt.show()

#Teste2
plt.figure(2) #Cria a janela onde o grafico numero 2 sera mostrado

plt.subplot(3,1,1) #Area do primeiro grafico
plt.axis((2,10,2,8))
plt.grid(True)
plt.plot(t_x_teste2, x_teste2, 'r*', label='x_teste2')
plt.xlabel('t')
plt.ylabel('x_teste2(t)')
plt.title('Teste2') #Nomear o primeiro grafico implica aqui em nomear o Teste por questao de estetica
plt.legend()

plt.subplot(3,1,2) #Area do segundo grafico
plt.axis((2,10,0,5))
plt.grid(True)
plt.plot(t_h_teste2, h_teste2, 'gD', label='h_teste2')
plt.xlabel('t')
plt.ylabel('h_teste2(t)')
plt.legend()

plt.subplot(3,1,3) #Area do terceiro grafico
plt.axis((2,10,5,32))
plt.grid(True)
plt.plot(indep_values_teste2, y_teste2, 'b^', label='y_teste2')
plt.xlabel('t')
plt.ylabel('y_teste2(t)')
plt.legend()

plt.show()

#Teste3
plt.figure(3) #Cria a janela onde o grafico numero 3 sera mostrado

plt.subplot(3,1,1) #Area do primeiro grafico
plt.axis((0,10,-7,7))
plt.grid(True)
plt.plot(t_x_teste3, x_teste3, 'r*', label='x_teste3')
plt.xlabel('t')
plt.ylabel('x_teste3(t)')
plt.title('Teste3') #Nomear o primeiro grafico implica aqui em nomear o Teste por questao de estetica
plt.legend()

plt.subplot(3,1,2) #Area do segundo grafico
plt.axis((0,10,-7,7))
plt.grid(True)
plt.plot(t_h_teste3, h_teste3, 'gD', label='h_teste3')
plt.xlabel('t')
plt.ylabel('h_teste3(t)')
plt.legend()

plt.subplot(3,1,3) #Area do terceiro grafico
plt.axis((0,10,-7,7))
plt.grid(True)
plt.plot(indep_values_teste3, y_teste3, 'b^', label='y_teste3')
plt.xlabel('t')
plt.ylabel('y_teste3(t)')
plt.legend()

plt.show()

#Teste4
plt.figure(4) #Cria a janela onde o grafico numero 4 sera mostrado

plt.subplot(3,1,1) #Area do primeiro grafico
plt.axis((2,10,0,5))
plt.grid(True)
plt.plot(t_x_teste4, x_teste4, 'r*', label='x_teste4')
plt.xlabel('t')
plt.ylabel('x_teste4(t)')
plt.title('Teste4 - Proprieade Comutativa') #Nomear o primeiro grafico implica aqui em nomear o Teste por questao de estetica
plt.legend()

plt.subplot(3,1,2) #Area do segundo grafico
plt.axis((2,10,0,8))
plt.grid(True)
plt.plot(t_h_teste4, h_teste4, 'gD', label='h_teste4')
plt.xlabel('t')
plt.ylabel('h_teste4(t)')
plt.legend()

plt.subplot(3,1,3) #Area do terceiro grafico
plt.axis((2,10,5,32))
plt.grid(True)
plt.plot(indep_values_teste4, y_teste4, 'bD', label='y_teste4')
plt.plot(indep_values_teste2, y_teste2, 'r^', label='y_teste2')
plt.xlabel('t')
plt.ylabel('y_teste4(t) e y_teste2')
plt.legend()

plt.show()

#Teste5
plt.figure(5) #Cria a janela onde o grafico numero 5 sera mostrado

plt.subplot(3,1,1) #Area do primeiro grafico
plt.axis((0,10,0,8))
plt.grid(True)
plt.plot(t_x_teste5, x_teste5, 'r*', label='x_teste5')
plt.xlabel('t')
plt.ylabel('x_teste5(t)')
plt.title('Teste5 - Proprieade Distributiva') #Nomear o primeiro grafico implica aqui em nomear o Teste por questao de estetica
plt.legend()

plt.subplot(3,1,2) #Area do segundo grafico
plt.axis((0,10,0,8))
plt.grid(True)
plt.plot(t_h_teste5, h_teste5, 'gD', label='h_teste5')
plt.xlabel('t')
plt.ylabel('h_teste5(t)')
plt.legend()

plt.subplot(3,1,3) #Area do terceiro grafico
plt.axis((0,10,30,125))
plt.grid(True)
plt.plot(indep_values_teste5, y_teste5, 'bD', label='y_teste5')
plt.plot(indep_values_teste5, [36,54,84,102,117,121,123,114,82,83,62,30], 'r^', label='soma das saidas1/4')
plt.xlabel('t')
plt.ylabel('y_teste5(t) e y_teste1+y_teste4')
plt.legend()

plt.show()

#Teste6
plt.figure(6) #Cria a janela onde o grafico numero 6 sera mostrado

plt.subplot(3,1,1) #Area do primeiro grafico
plt.axis((0,5,0,10))
plt.grid(True)
plt.plot(t_x_teste6, x_teste6, 'r*', label='x_teste6')
plt.xlabel('t')
plt.ylabel('x_teste6(t)')
plt.title('Teste6 -Impulso como elemento neutro da convolucao') #Nomear o primeiro grafico implica aqui em nomear o Teste por questao de estetica
plt.legend()

plt.subplot(3,1,2) #Area do segundo grafico
plt.axis((0,5,0,10))
plt.grid(True)
plt.plot(t_h_teste6, h_teste6, 'gD', label='h_teste6')
plt.xlabel('t')
plt.ylabel('h_teste6(t)')
plt.legend()

plt.subplot(3,1,3) #Area do segundo grafico
plt.axis((0,5,0,10))
plt.grid(True)
plt.plot(indep_values_teste6, y_teste6, 'rD', label='y_teste6')
plt.xlabel('t')
plt.ylabel('y_teste6(t)')
plt.legend()

plt.show()