import numpy as np
from sympy import *
from math import *

def pivotacaoParcial(A,y):

    p = 0
    m = []
    max = -1

    for i in range(0,A.shape[0]):
        max = i
        for j in range(i+1,A.shape[0]):
            if abs(A[max,i]) < abs(A[j,i]): # se o item atual for maior do que o item da linha atual, a linha atual contém o maior pivô
                max = j
        if(max >=0 ): # se houve alguma troca, troca a linha atual com a linha de índice guardado na variável max
            p += 1
            Temp = np.copy(A[i])
            A[i] = np.copy(A[max])
            A[max] = np.copy(Temp)
            Temp2 = np.copy(y[max])
            y[max] = np.copy(y[i])
            y[i] = Temp2
            if(i > 0):
                Temp3 = m[len(m) - (A.shape[0] - i) + (max - i)]
                m[len(m) - (A.shape[0] - i) + (max - i)] = m[len(m) - (A.shape[0] - i)]
                m[len(m) - (A.shape[0] - i)] = Temp3

        max=-1 # retorna max para seu valor inicial

        for k in range(i+1,A.shape[0]): # calcula o coeficiente d para a anulação dos itens abaixo da diagonal, uma coluna por vez. Seu valor é multiplicado por -1 e guardado em m
            d = np.copy(A[k,i])
            d = d/np.copy(A[i,i])
            m.append(d)
            A[k,:] = np.copy(A[k,:]) - (np.copy(A[i,:])*d)

    return [A,p,m,y] # retorna a matriz A orginal, a quantidade de permutações de linha p e os coeficientes da pivotação, multiplicados por -1

def resolverTriangularInferior(A):
    R = np.transpose(np.copy(A[:,A.shape[1]-1]))# copia e transpõe os valores independentes do sistema
    for i in range(0,A.shape[0]):
            for j in range(0,i):
                R[i] = np.copy(R[i]) - np.copy(A[i,j]) # ax1 + b = c -> [ ax1 = c - b ]
                A[i,j] = 0
            R[i] = (np.copy(R[i])/np.copy(A[i,i])) # x1 = (c - b) / a
            A[i,i] = 1
            A[i+1:,i] = np.copy(A[i+1:,i])*np.copy(R[i])
# multiplica as linhas de cima, da coluna atual, pelo valor descoberto de 'Xi'
    return [A,R] # retorna a matriz final e o vetor de resultados. Se tudo correr bem, A deve ser uma matriz identidade

def eliminacaoDeGauss(A):

        R = np.transpose(np.copy(A[:,A.shape[1]-1])) # copia e transpõe os valores independentes do sistema
        for i in range(A.shape[0]-1,-1,-1):

                for j in range(A.shape[0]-1,i,-1):

                     R[i] = np.copy(R[i]) - np.copy(A[i,j]) # ax1 + b = c -> [ ax1 = c - b ]
                     A[i,j] = 0

                R[i] = (np.copy(R[i])/np.copy(A[i,i])) # x1 = (c - b) / a
                A[i,i] = 1

                A[:i,i] = np.copy(A[:i,i])*np.copy(R[i]) # multiplica as linhas de cima, da coluna atual, pelo valor descoberto de 'Xi'

        return [A,R] # retorna a matriz final e o vetor de resultados. Se tudo correr bem, A deve ser uma matriz identidade

A = np.matrix(eval(input("Digite uma matriz : ")))
B = np.matrix(eval(input("Digite os termos independentes a serem testados: ")))
B = B.astype(float)
A = A.astype(float)
y = None # inicialização de y

for k in range(0,B.shape[0]):

    y = np.transpose(np.copy(B[k,:])) # escolhe uma das linhas de termos independentes

    P = pivotacaoParcial(np.copy(A),np.copy(y)) # transforma a matriz A em triangular superior com pivotação parcial
    y = P[3] # y recebe temporariamente o vetor b
    m = P[2] # array dos coeficientes da pivotação
    P = P[0] # matriz triangular superior resultante da pivotação
    L = np.identity(A.shape[0]) # matriz L
    L = L.astype(float)

    for q in range(0,P.shape[0]-1): # colocando os coeficientes da pivotação na matriz L
        for j in range(q+1,P.shape[0]):
            L[j,q] = m[0] 
            m.pop(0)

    L = np.hstack((np.copy(L),np.copy(y))) # adiciona o vetor b como coluna de L

    y = resolverTriangularInferior(np.copy(L))[1] # Ly = b

    U = np.copy(P) # matriz U

    U = np.hstack((np.copy(U),np.copy(np.transpose(np.asmatrix(y))))) # adiciona o y como coluna de U

    R = eliminacaoDeGauss(np.copy(U)) # Ux = y

    print("\n-> Resposta "+str(k+1)+" da Fatoração LU:")
    print(R[1]) # vetor resposta de U para o y da iteração
    print("L: \n\n",L)
    print("U: \n\n",U)
