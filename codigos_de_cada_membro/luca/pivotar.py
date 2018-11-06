import numpy as np

def pivotar(A):

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
            print(A[k,:])
                
    return [A,p]

A = np.matrix(input("Digite uma matriz quadrada: "))
A = A.astype(float)
R = pivotar(A)

print(R[0])
print(R[1])
