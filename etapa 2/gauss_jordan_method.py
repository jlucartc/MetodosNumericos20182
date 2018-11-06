import sys
import numpy as np
from timeit import default_timer as timer

def gauss_jordan_method(A, b, partial_pivot = False):
    start = timer()
    N = A.shape[0]  # Número de linhas da matriz A.
    M = A.shape[1]  # Número de colunas da matriz A.
    I = np.identity(N)  # Matriz identidade N x N. Por padrão, dtype é float.

    print("Matrix A:")
    print(A)

    print("\nVector b:")
    print(b)

    for j in range(M):  # Colunas que têm elementos a serem zerados.
        if partial_pivot:
            biggest_pivot = abs(A[j, j])
            line_biggest_pivot = j

            for k in range(j + 1, N):  # Encontrando o pivô com maior módulo.
                if abs(A[k, j]) > biggest_pivot:
                    biggest_pivot = abs(A[k, j])
                    line_biggest_pivot = k

            if line_biggest_pivot != j:  # Troca de linhas.
                line = A[j].copy()
                A[j] = A[line_biggest_pivot]
                A[line_biggest_pivot] = line

                line = I[j].copy()
                I[j] = I[line_biggest_pivot]
                I[line_biggest_pivot] = line

                line = b[0, j].copy()
                b[0, j] = b[0, line_biggest_pivot]
                b[0, line_biggest_pivot] = line

        auxiliary = A[j, j].copy()

        for k in range(M):
            A[j, k] = A[j, k] / auxiliary
            I[j, k] = I[j, k] / auxiliary

        b[0, j] = b[0, j] / auxiliary

        for i in range(N):  # Linhas nas quais estes elementos (a serem zerados) estão.
            if i != j:
                m = (-1) * A[i, j]

                for k in range(M):  # Atualização da linha.
                    A[i, k] = m * A[j, k] + A[i, k]
                    I[i, k] = m * I[j, k] + I[i, k]

                b[0, i] = m * b[0, j] + b[0, i]

    print("\nMatrix A as identity:")
    print(A)

    print("\nSolution found:")
    print(b)

    print("\nInverse matrix of A:")
    print(I)

    end = timer()
    print("\nRuntime: %.6e seconds." % (end - start))
    return b


gauss_jordan_method(A = np.array(np.mat(sys.argv[1]), dtype = float),
                    b = np.array(np.mat(sys.argv[2]), dtype = float),
                    partial_pivot = str(sys.argv[3]).lower() == "pp")
