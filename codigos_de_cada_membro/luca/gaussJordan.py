import numpy as np
from sympy import *
from math import *


def pivotacaoParcial(A,I):

    p = 0
    m = None

    for i in range(0,A.shape[0]):
        for j in range(i+1,A.shape[0]):
            if A[i,i] < A[j,i]:
                p += 1
                Temp = np.copy(A[i])
                A[i] = np.copy(A[j])
                A[j] = np.copy(Temp)
                Temp2 = np.copy(I[i])
                I[i] = np.copy(I[j])
                I[j] = np.copy(Temp2)

        for k in range(i+1,A.shape[0]):
            d = np.copy(A[k,i])
            d = d/np.copy(A[i,i])
            A[k,:] = np.copy(A[k,:]) - (np.copy(A[i,:])*d)
                
    return [A,p,I]
        
def triangularSuperiorGaussJordan(A,I):
        for i in range(A.shape[0]-1,0,-1):
            for j in range(i-1,-1,-1):
                d = np.copy(A[j,i])/np.copy(A[i,i])
                A[j] = np.copy(A[j]) - np.copy(A[i])*d
                I[j] = np.copy(I[j]) - np.copy(I[i])*d
        R = np.copy(A[:,A.shape[1]-1])
        for k in range(0,A.shape[0]):
            R[k] = np.copy(R[k])/np.copy(A[k,k])
            I[k,:] = np.copy(I[k,:])/np.copy(A[k,k])
        return [A,I,R]

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

      Ts = pivotacaoParcial(np.copy(A),np.copy(I)) # transforma a matriz A em triangular superior com pivotação parcial 
      p = Ts[1]
      I = Ts[2]
      Ts = Ts[0]

      gaussJordan = triangularSuperiorGaussJordan(np.copy(Ts),np.copy(I)) #transforma a matriz A em matriz diagonal

      print("Resultado por eliminação de Gauss-Jordan: \n\n")
      print(gaussJordan[2])




        
    
