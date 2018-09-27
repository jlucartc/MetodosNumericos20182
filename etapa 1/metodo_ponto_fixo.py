from sympy import*

from math import *

import matplotlib.pyplot as plt #plot

x = symbols('x')

print("-- Método do ponto fixo --")

phix = sympify((str)(input("Digite phi(x): ")))

fx = sympify((str)(input("Digite f(x): ")))

x0 = (float)(input("Digite x0: "))

e = (float)(input("Digite o valor da precisão: "))

c = 0
i = 300 # iteracoes

while (c < i) :

    phi = phix.subs(x,x0)

    if(abs(fx.subs(x,x0)) < e):

        print("-> Raiz = "+str(phi))
        print("i : "+str(c))
        break

    x0 = phi
    
    if(c == i-1):
        print("-> Número máximo de iterações atingido")
        print("-> Último x0: "+str(x0))
    c+=1
