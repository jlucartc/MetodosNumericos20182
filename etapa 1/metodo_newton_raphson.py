from sympy import*

import math

import time

import matplotlib.pyplot as plt #plot

x = symbols('x')

print("\n\n-- Método de Newton-Raphson --\n")

fx = sympify((str)(input("Digite f(x): "))) # recebe a função

dfx = diff(fx,x) # calcula a derivada da função recebida

x0 = (float)(input("Digite x0: ")) # recebe o ponto inicial

def phix(a, b, c): # define função phi(x)

    return a - (b.subs(x,x0)/c.subs(x,x0))

e = (float)(input("Digite o valor da precisão: ")) # recebe o valor da precisão
c = 0 # inicia contador de iterações

start = time.time()
end = 0

while (c < 30) :

    phi = phix(x0,fx,dfx) # calcula phi(x0)

    if(abs(fx.subs(x,x0)) < e): # checa se a função em x0 é menor ou igual à precisão desejada

        end = time.time() # calcula tempo final

        print("-> Raiz = "+str(float(phi))) # imprime a raiz encontrada
        print("-> iterações: "+str(c)) # imprime o número de iterações
        break # sai do laço

    x0 = phi # caso f(x) não seja perto de 0 o suficiente, x0 recebe o valor de phi(x0) e segue no laço
    
    if(c == 29):

        end = time.time() # calcula tempo final
        
        print("-> Número máximo de iterações atingido")
    
    c+=1

print("-> Tempo de execução: "+str(end - start)+" segundos\n\n") # imprime o tempo de execução na tela


