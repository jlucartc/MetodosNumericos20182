import sys
import numpy as np
from timeit import default_timer as timer

def norm(v, x):
    n = v.shape[1]  # Número de colunas do vetor (k + 1).
    maximum_numerator = 0
    maximum_denominator = 0

    for i in range(n):
        # Colhendo a maior diferença modular entre os elementos dos vetores (k +1) e k.
        if abs(v[0, i] - x[0, i]) > maximum_numerator:
            maximum_numerator = abs(v[0, i] - x[0, i])

        # Colhendo o maior elemento do vetor (k + 1).
        if abs(v[0, i]) > maximum_denominator:
            maximum_denominator = abs(v[0, i])

    return maximum_numerator / maximum_denominator


def gauss_seidel_method(A, b, e, max_interactions):
    start = timer()
    print("Matrix A:")
    print(A)

    print("\nVector b:")
    print(b)

    n = b.shape[1]  # Número de colunas do vetor b.

    # Inicialmente, os vetores (k + 1) e k e a matriz C terão apenas zeros.
    v = np.zeros((1, n))
    x = np.zeros((1, n))
    C = np.zeros((n, n))

    g = b.copy()  # O vetor g assume os mesmos elementos do vetor b.

    for i in range(n):  # Gerando a matriz C e o vetor g.
        for j in range(n):
            if i != j:
                C[i, j] = ((-1) * A[i, j]) / A[i, i]

        g[0, i] = g[0, i] / A[i, i]

    k = 1

    print("\nMatrix C:")
    print(C)

    print("\nVector g:")
    print(g)

    while k <= max_interactions:
        for i in range(n):  # Atualizando o vetor (k + 1).
            partial_sum = 0

            for j in range(n):
                partial_sum += C[i, j] * v[0, j]

            v[0, i] = partial_sum + g[0, i]

        if norm(v, x) < e:  # Checando se a precisão foi atingida por meio da norma.
            print("\nSolution found:")
            print(v)

            end = timer()
            print("\nRuntime: %.6e seconds in %d interactions." % ((end - start), k))
            return v

        x = v.copy()
        k += 1

    # Corrigindo o número de interações quando a precisão não é atingida durante o while.
    if k == max_interactions + 1:
        k -= 1

    end = timer()
    print("\nRuntime: %.6e seconds in %d interactions." % ((end - start), k))
    return v


gauss_seidel_method(A = np.array(np.mat(sys.argv[1]), dtype = float),
                    b = np.array(np.mat(sys.argv[2]), dtype = float),
                    e = float(sys.argv[3]),
                    max_interactions = 50)
