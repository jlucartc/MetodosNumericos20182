import numpy as np
from sympy import *
from math import *

from timeit import default_timer as timer

start = None
end = None

def maxXi(Xn,X):

    n = None
    d = None

    for i in range(Xn.shape[0]):

        if(np.copy(Xn[i,0]) != 0):
            nk = abs(np.copy(Xn[i,0]) - np.copy(X[i,0]))/abs(np.copy(Xn[i,0]))
        dk = abs(np.copy(Xn[i,0]))
        
        if n == None or nk > n:

            n = nk

        if d == None or dk > d:

            d = dk

    return n/d


A = np.matrix(eval(input("Digite uma matriz : ")))
A = A.astype(float)
X = np.matrix(eval(input("Digite X : ")))
e = float(input("Digite a precisão: "))

B = np.copy(A[:,A.shape[1]-1])
A = np.delete(np.copy(A),A.shape[1]-1,1)

C = np.asmatrix(np.zeros([A.shape[0],A.shape[1]]))
C = C.astype(float)
G = np.copy(B)

for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        if i != j:
            C[i,j] = (np.copy(A[i,j])/np.copy(A[i,i]))*(-1)
    G[i,0] = (np.copy(G[i,0]))/(np.copy(A[i,i]))
    C[i,i] = 0
Xn = None
z = True

print("Matriz C:\n",C)
print("Matriz G:\n",G)

start = timer()

while(z):

    Xn = (np.copy(C) @ np.copy(X)) + np.copy(G)

    d = maxXi(np.copy(Xn),np.copy(X))

    if(d < e):
        z = False
    else:
        X = np.copy(Xn)

end = timer()

print("Resposta de Gauss-Jacobi: ")
print(Xn)
print("Tempo de execucao total: %e segundos" % (end - start))
