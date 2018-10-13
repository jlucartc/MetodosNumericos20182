import numpy as np
from sympy import *
from math import *


def pivotacaoParcial(A):

    p = 0
    m = None

    for i in range(0,A.shape[0]):
        for j in range(i+1,A.shape[0]):
            if A[i,i] < A[j,i]:
                p += 1
                Temp = np.copy(A[i])
                A[i] = np.copy(A[j])
                A[j] = np.copy(Temp)
                
        for k in range(i+1,A.shape[0]):
            d = np.copy(A[k,i])
            d = d/np.copy(A[i,i])
            A[k,:] = np.copy(A[k,:]) - (np.copy(A[i,:])*d)
                
    return [A,p]

def eliminacaoDeGauss(A):

    R = np.asmatrix([0]*A.shape[0]) # matriz de valores das icógnitas
    R = R.astype(float)

    for i in range(A.shape[0]-1,-1,-1):

        R[0,i] = np.copy(R[0,i]) + np.copy(A[i,A.shape[0]])

        for j in range(A.shape[0]-1,i,-1):

            R[0,i] = np.copy(R[0,i]) - np.copy(A[i,j])

        R[0,i] = (np.copy(R[0,i])/np.copy(A[i,i]))

        A[:,i] = np.copy(A[:,i])*np.copy(R[0,i])


    return [A,R]

A = np.matrix(eval(input("Digite uma matriz : ")))
A = A.astype(float)
print("Linhas: "+str(A.shape[0]))
ERR = False

if(A.shape[0] != A.shape[1]-1): # checa se a matriz é quadrada

    ERR = True;

    
if(ERR):

    print("-> Matriz inválida.") # O programa encerra por conta de entrada inválida

else:

      Ts = pivotacaoParcial(np.copy(A)) # transforma a matriz A em triangular superior com pivotação parcial 
      p = Ts[1]
      Ts = Ts[0]

      eliminacaoDeGauss = eliminacaoDeGauss(np.copy(Ts))

      print("\nResultado por eliminação de Gauss: \n\n")
      print(eliminacaoDeGauss[1])
      



        
    
