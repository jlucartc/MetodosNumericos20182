import sys
import numpy as np
from timeit import default_timer as timer

start = None
end = None

A = np.asmatrix(sys.argv[1])
A = A.astype(float)
I = np.identity(A.shape[0], dtype=float)
N = np.concatenate((A, I),axis=1)

start = timer()
# itera as colunas
for c in range(0, A.shape[1] - 1):
    #procura coluna pivô não nula
    if (N[c,c] == 0.0):
        for l in range(c + 1, A.shape[0]):
            if (N[l, c] != 0.0):
                temp = np.copy(N[c, :])
                N[c, :] = np.copy(N[l, :])
                N[l, :] = np.copy(temp)
    #torna o pivo igual a 1
    if (N[c,c] != 1):
        N[c, :] = N[c,:]/N[c,c]
    #zera os elementos abaixo do pivo
    for l in range(c + 1, A.shape[0]):
        N[l, :] = N[l, :] - N[l,c] * N[c, :]
    #zera os elementos acima do pivo
    if (c-1 >= 0):
        for l in range(c - 1,-1,-1):
            N[l, :] = N[l, :] - N[l, c] * N[c, :]

#print("Matriz A:")
#print(N[:,:A.shape[1]-1])
end = timer()
print("Matriz Inversa:")
print(N[:,A.shape[1]:])
print("\nSolucao encontrada:")
print(N[:,A.shape[1]-1])
print("Tempo de execucao total: %e segundos" % (end - start))
