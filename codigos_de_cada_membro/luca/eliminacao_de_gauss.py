import numpy as np
from sympy import *
from math import *

def triangularSuperior(A,I): # gera a matriz triangular superior

    for i in range(0,A.shape[0]): # linha pivot
        for j in range(i+1,A.shape[0]): # linha sendo modificada pelo pivot
             d = A[j,i]/A[i,i]
             A[j] = A[j] + A[i]*(-d)
             #I[j] = I[j] + A[i]*(-d)

    return A

def resolveTriangular(A):

    R = np.asmatrix([0]*A.shape[0]) # matriz de valores das icógnitas
    R = R.astype(float)

    for i in range(A.shape[0]-1,-1,-1):

        R[0,i] = R[0,i] + A[i,A.shape[0]]

        for j in range(A.shape[0]-1,i,-1):

            print("Laço "+str(i))

            R[0,i] = R[0,i] - A[i,j]

        R[0,i] = (R[0,i]/A[i,i])

        A[:,i] = A[:,i]*R[0,i]

        print(R)


    return R
        
        
        

A = np.matrix(eval(input("Digite uma matriz : ")))
A = A.astype(float)
print("Linhas: "+str(A.shape[0]))
I = np.matrix([(0,0),(0,0)]) # Matriz identidade ainda não criada devidamente
I = I.astype(float)
ERR = False

if(A.shape[0] != A.shape[1]-1): # checa se a matriz é quadrada

    ERR = True;

    
for i in range(0,A.shape[0]):
    
    # criando matriz identidade para obtenção da matriz inversa de A
    I = np.asmatrix(np.identity(3))
    
if(ERR):

    print("-> Matriz inválida.") # O programa encerra por conta de entrada inválida

else:

      Ts = triangularSuperior(A,I);

      R = resolveTriangular(Ts);

      print(R)



        
    
