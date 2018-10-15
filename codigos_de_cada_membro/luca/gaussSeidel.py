#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from sympy import *
from math import *

def maxXi(Xn,X):

    n = None
    d = None

    for i in range(Xn.shape[0]):

        nk = abs(Xn[i,0] - X[i,0])
        dk = abs(Xn[i,0])
        
        if n == None or nk > n:

            n = nk

        if d == None or dk > d:

            d = dk


    return n/d


A = np.matrix(eval(input("Digite uma matriz : ")))
A = A.astype(float)
X = np.matrix(eval(input("Digite X : ")))
X = X.astype(float)
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

CX = np.copy(X)
z = True
c = 0

print(C)

while(z):

    mX = []

    Y = np.copy(X)

    for i in range(0,X.shape[0]):

        xN = np.dot(np.copy(C[i,:]),Y) + np.copy(G[i,0])# calcula xn

        xN = xN 

        Y[i,0] = xN[0,0]

        print("Y: ",Y)
        print("xN",xN[0,0])

    XN = np.copy(Y)

    d = maxXi(np.copy(XN),np.copy(X))

    if(d < e or c > 300):
        z = False
    else:
        X = np.copy(XN)
        c+=1

print("Resposta de Gauss-Jacobi: ")
print(XN)

