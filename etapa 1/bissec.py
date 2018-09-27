from sympy import*

import matplotlib.pyplot as plt #plot

x = symbols('x')

difF = "x**3 - 9*x + 3"

print("-- Método da bisseção --")
expr = input("Digite a expressão a ser analizada: ")
a = float(input("Digite o limite do intervalo pela esquerda: "))
b = float(input("Digite o limite do intervalo pela direita: "))
e = float(input("Digite a precisão desejada: "))
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

c=1
z = 300
#plote

while z != 0:

    la = expr.subs(x,a)
    lb = expr.subs(x,b)
    m = ((b-a)/2.0)
    fm = expr.subs(x,(a + m))
    aa.append(a) #plot
    ba.append(b) #plot
    c+=1
    z-=1
    
    if (la * lb) >= 0:
        #Encerra o laço
        print("Intervalo inválido")
        z = 0
        break
    else:
        if (((fm**2)**(0.5)) <= e):
            print("Iterações: "+str(c))
            print("Raiz: "+str(a+m))
            rp[0] = a+m #plot
            rp[1] = expr.subs(x,a+m) #plot
            break
        elif ( lb * fm ) < 0:
            a = a + m
        else:
            b = b - m
            
    if (z == 0) :
        print("Iterações: "+str(c))
        print("Ultima raiz: "+str(lm))
        rp[0] = a+m #plot
        rp[1] = expr.subs(x,a+m) #plot

#ploti
plt.plot(xa,ya,xa,za,'k',rp[0],rp[1],'bo')
'''
for i in range(0,len(aa)-1) :
    plt.plot(aa[i],ba[i],'r--')
'''

plt.show()
#plote
