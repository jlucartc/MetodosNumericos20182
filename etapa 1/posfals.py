from sympy import *

import matplotlib.pyplot as plt #plot

from matplotlib.animation import FuncAnimation

from timeit import default_timer as timer

x = symbols('x')

difF = "x**3 - 9*x + 3"

print("-- Método da posição falsa --")
expr = input("Digite a expressão a ser analizada: ")
a = float(input("Digite o limite do intervalo pela esquerda: "))
b = float(input("Digite o limite do intervalo pela direita: "))
e = float(input("Digite a precisão deejada: "))
c = 1
z = 300

if(len(expr) == 0):
    expr = sympify(difF)
else:
    expr = sympify(expr)
#ploti
xa = [a]
ya = [expr.subs(x,a)]
aa = []
ba = []
za = [0]
rp = [0,0]

n = 10 #q. de pontos

p = (b-a)/(n-1) # passo

while (n-1) != 0:
    xa.append(round(a+(p*c),2))
    ya.append(round(expr.subs(x,xa[len(xa)-1]),2))
    za.append(0)
    c+=1
    n-=1

c=0
z = 300
#plote

while z != 0:

        fa = expr.subs(x,a)
        fb = expr.subs(x,b)
        x0 = (a*fb - b*fa)/(fb - fa)
        fx0 = expr.subs(x,x0)
        aa.append(a) #plot
        ba.append(b) #plot
        c+=1
        z-=1
        
        if(abs(fx0) <= e):
            print("Iterações: "+str(c))
            print("Raiz: "+str(x0))
            rp[0] = x0 #plot
            rp[1] = expr.subs(x,x0) #plot
            z = 0
            break
        else:
            if fa > fb:
                b = x0
            else:
                a = x0

        if(z == 0):
            print("Iterações: "+str(c))
            print("Ultima raiz: "+str(x0))
            rp[0] = x0 #plot
            rp[1] = expr.subs(x,x0) #plot
            
#ploti
plt.plot(xa,ya,xa,za,'k',rp[0],rp[1],'bo')
'''
for i in range(0,len(aa)-1) :
    plt.plot(aa[i],ba[i],'r--')
'''

plt.show()
#plote
