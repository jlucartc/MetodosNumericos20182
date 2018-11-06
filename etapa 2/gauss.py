import sys
from timeit import default_timer as timer
import numpy as np

start = None
end = None

def solveTriang(A, b):
    N = A.shape[0]
    x = np.zeros(N)

    print("Matriz A:")
    print(A)
    print("\nVetor b:")
    print(b)

    for i in range(N-1,-1,-1):
        partialSum = 0.0
        for j in range(i+1,N):
            partialSum += A[i, j] * x[j]
        x[i] = (b[i] - partialSum) / A[i, i]

    print("\nSolucao encontrada:")
    print(x[:, None])

    print("\nVetor de residuos:")
    print(b - A @ x)

    return x

M = np.asmatrix(sys.argv[1])
M = M.astype(float)
A = np.copy(M)
k = None
#Bi = np.copy(M[:,M.shape[1]-1])

start = timer()
#itera as colunas
for c in range(0, A.shape[1]-1):
    #itera as linhas e encontra maior na coluna
    maior = abs(A[c, c])
    for l in range(c+1, A.shape[0]):
        if (abs(A[l,c]) > maior):
            k=l
            maior = abs(A[l,c])
    #troca linha atual por linha com maior
    if (k != c and abs(A[c,c])!= maior):
        temp = np.copy(A[c,:])
        A[c,:] = np.copy(A[k,:])
        A[k,:] = np.copy(temp)
        #print("\nTroca de linhas %s com %s:"%(k,c))
    
    for l in range(c+1, A.shape[0]):
        z = A[l,c]/A[c,c]
        A[l,:] = A[l,:] - z*A[c,:]

b = np.copy(A[:,A.shape[1]-1])
solveTriang(A[:,:A.shape[1]-1],b)
end = timer()
print("Tempo de execucao total: %e segundos" % (end - start))
