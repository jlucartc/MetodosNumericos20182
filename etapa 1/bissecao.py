# -*- coding: utf-8 -*-

import math
from timeit import default_timer as timer

# Função para calcular f(x)
def funcao(x):
	return 1/(((x-0.3)**2) + 0.01) - 1/(((x-0.8)**2) + 0.04) 



# Definir intervalo inicial
a = float(input("Digite o intervalo a: "))
b = float(input("Digite o intervalo b: "))


# Definir precisao e numero maximo de interações
precisao = 10**-2 
maxInter = 50

Fa = funcao(a)
Fb = funcao(b)

if(Fa * Fb < 0):
	
	if(Fa == 0):
		x = a
	
	if(Fb == 0):
		x = b	

	if(abs(b-a) < precisao):
		x = a
	
	else:
		
		str_iter = 'Iteração'
		str_a = 'a'
		str_fa = 'f(a)'
		str_b = 'b'
		str_fb = 'f(b)'
		str_x = 'x'
		str_fx = 'f(x)'
		str_inter = 'Intervalo'
		
		
		print("{0:^16}".format(str_iter) + "|{0:^14}".format(str_a) + "|{0:^14}".format(str_fa) + "|{0:^14}".format(str_b) + "|{0:^14}".format(str_fb) + "|{0:^14}".format(str_x) + "|{0:^14}".format(str_fx) + "|{0:^14}".format(str_inter))
		
		for i in range(1,maxInter+1):

			x = float(a+b)/2
			Fx = funcao(x)
			
			if(abs(b-a) < precisao) or (Fx == 0): 
				break
			
			if(Fa * Fx < 0):
				b = x
				
			else:
				a = x
			
			print("{0:^14}".format(i) + "|{0:^14.6e}".format(a) + "|{0:^14.6e}".format(Fa) + "|{0:^14.6e}".format(b) + "|{0:^14.6e}".format(Fb) + "|{0:^14.6e}".format(x) + "|{0:^14.6e}".format(Fx) + "|{0:^14.6e}".format(abs(b-a)))

	print("\nValor da raiz: %f" % (x))	
	
else:
	print("\nIntervalo mal definido")	
