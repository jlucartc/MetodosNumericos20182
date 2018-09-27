# -*- coding: utf-8 -*-
import math
#Função que calcula f(x)
def funcao(x):
	return math.cosh(x) * math.cos(x) 

#Definir o intervalo inicial
a = float(input("Digite o intervalo a: "))
b = float(input("Digite o intervalo b: "))
print("\n")

e = 10**-5
iterMax = 20

Fa = funcao(a)
Fb = funcao(b)

#Verificar se o intervalo é válido
if Fa*Fb < 0:
	
	#Verificar se os parâmetros passados já satisfazem a precisão

	if(Fa == 0):
		raiz = a
	if(Fb == 0):
		raiz = b
		
	if(abs(b - a) > e):
		k = 1
		

		str_iter = 'Iteração'
		str_a = 'a'
		str_fa = 'f(a)'
		str_b = 'b'
		str_fb = 'f(b)'
		str_x = 'x'
		str_fx = 'f(x)'
		str_inter = 'Intervalo'

		print("{0:^16}".format(str_iter) + "|{0:^14}".format(str_a) + "|{0:^14}".format(str_fa) + "|{0:^14}".format(str_b) + "|{0:^14}".format(str_fb) + "|{0:^14}".format(str_x) + "|{0:^14}".format(str_fx) + "|{0:^14}".format(str_inter))		

		#Iterações que vão calcular a raiz
		for i in range(1,iterMax+1):

			#Calculo da "posição falsa" 
			x = (a*Fb - b*Fa)/(Fb - Fa)
			Fx = funcao(x)
			
			intervalo = abs(b-a)

			print("{0:^14}".format(i) + "|{0:^14.6e}".format(a) + "|{0:^14.6e}".format(Fa) + "|{0:^14.6e}".format(b) + "|{0:^14.6e}".format(Fb) + "|{0:^14.6e}".format(x) + "|{0:^14.6e}".format(Fx) + "|{0:^14.6e}".format(intervalo))
			
			#Verificar se a raiz foi encontrada			
			if(intervalo < e or abs(Fx) < e or Fx == 0):
				raiz = x
				break

			#Verificar em qual lado de 'x' está a raiz

			if(Fa*Fx < 0):
				b = x
				Fb = Fx
			else:
				a = x
				Fa = Fx

			
			k = k + 1

		print("\nA raiz é: %f " % raiz)
	else:
		raiz = a
		print("\nA raiz é: %f" % raiz)			
	
else:
	print("Intervalo Inválido")
