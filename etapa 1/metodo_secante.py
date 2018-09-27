from sympy import*

import matplotlib.pyplot as plt #plot

x = symbols('x')

print("-- Método da secante --")

fx = sympify((str)(input("Digite f(x): ")))

dfx = diff(fx,x)

x0 = (float)(input("Digite x0: "))

x1 = (float)(input("Digite x1: "))

def phixS(a0,a1,b,c):

    return a0 - b.subs(c,a0)/((b.subs(c,a1) - b.subs(c,a0))/(a1 - a0))

e = (float)(input("Digite o valor da precisão: "))

c = 0
n = 0

while (c < 35) :

    n+=1

    phi = phixS(x0,x1,fx,x)

    if(abs(fx.subs(x,x0)) < e):

        print("-> Raiz = "+str(phi))
        print("i : "+str(n))
        break

    x0 = x1
    x1 = phi

    if(c == 29):
        print("-> Número máximo de iterações atingido")

    c+=1
