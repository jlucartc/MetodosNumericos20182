def criar_vetor_b(n):

    b = []

    for i in range(n):
        b.append(0)

    return b

def printar_vetor(x,n):
    '''

    :param x: Vetor que será printado
    :param n: tamanho do vetor
    :return: None
    '''

    print("")

    for i in range(n):
        print("{:5}".format(x[i]))

    print("")
    return None

def criar_matriz_quadrada(n):
    #:param n: Dimensao da Matriz
    #:return: A - Matriz diagonal
    A = []

    for i in range(0,n):

        linha = []

        for j in range(0,n):

            linha.append(0)

        A.append(linha)

    return A

def criar_matriz_diagonal(n):
    A = []

    for i in range(n):

        linha = []

        for j in range(n):

            if i != j:
                linha.append(0)
            else:
                linha.append(1)

        A.append(linha)

    return A

def printar_matriz(A,n,m):

    '''
    :param A: Matriz
    :param n: Número de linhas
    :param m: Número de colunas
    :return: None
    '''

    print("")

    if n != m:

        for i in range(n):

            for j in range(m):

                if j < m-1:
                    print("{:10.3e}".format(A[i][j]), end=" ")
                else:
                    print(" | " + "{:10.3e}".format(A[i][j]), end=" ")


            print("")

    else:

        for i in range(n):
            for j in range(n):
                print("{:10.3e}".format(A[i][j]), end=" ")
            print("")

    print("\n")
    return None

def add_coluna(A,c,n):
    '''

    :param A: Matriz original
    :param c: Nova coluna
    :param n: Dimensao - supondo matriz quadrada
    :return: M - Matriz com nova coluna
    '''

    M = []

    for i in range(n):

        linha = []

        for j in range(n+1):

            if j < n:
                linha.append(A[i][j])
            else:
                linha.append(c[i])

        M.append(linha)

    return M

def matrizes_LU(A,n,b,pp):
    U = A
    L = criar_matriz_diagonal(n)

    if pp > 0:

        LU = pivotamento_parcial(A,b,n)

        for i in range(n):

            for j in range(n):

                if i <= j:
                    U[i][j] = LU[i][j]

                else:
                    L[i][j] = LU[i][j]

            b[i] = LU[i][n]


    else:

        for k in range(n):

            for i in range(k+1, n):

                x = -(U[i][k] / U[k][k])

                U[i][k] = 0

                for j in range(k+1, n):
                    U[i][j] = U[i][j] + x*U[k][j]

                L[i][k] = -x

    #Printando matrizes

    print("Matriz L:")
    printar_matriz(L,n,n)
    print("Matriz U:")
    printar_matriz(U,n,n)

    #Resolvendo Ly = b
    y = resolver_triangular_inferior(L,b,n)

    #Resolvendo Ux = y
    x = resolver_triangular_superior(U,y,n)

    return x

def resolver_triangular_superior(A,b,n):

    x = criar_vetor_b(n)

    n = n-1

    x[n] = b[n]/A[n][n]

    for k in range(n-1,-1,-1):
        a = 0

        for j in range(k+1,n+1):
            a += A[k][j]*x[j]

        x[k] = (b[k] - a)/A[k][k]


    return x

def resolver_triangular_inferior(L,b,n):
    '''

    :param L: Matriz L
    :param b: Vetor b
    :param n: Tamanho de matriz n
    :return: y - Vetor solução de Ly = b
    '''

    y = criar_vetor_b(n)

    y[0] = b[0]/L[0][0]

    for k in range(1,n):
        a = 0
        for j in range(k):
            a += L[k][j]*y[j]

        y[k] = (b[k] - a)/L[k][k]


    return y

def pivotamento_parcial(A,b,n):
   LU = A

   for k in range(n):

       linha = -1

       aux = A[k][k]
       #Verificando o maior elemento na coluna k
       for l in range(k+1,n):
           if aux < A[l][k]:
               aux = A[l][k]
               linha = l
       #Colocar o maior elemento como pivô
       if l != -1:

           for c in range(n):
               aux = A[k][c]
               A[k][c] = A[linha][c]
               A[linha][c] = aux

           aux = b[linha]
           b[linha] = b[k]
           b[k] = aux

       #Fazer a fatoração LU
       #Nesse caso a Matriz LU é a matriz L+U
       for i in range(k+1,n):

            x = -(A[i][k]/A[k][k])

            LU[i][k] = -x

            for j in range(k+1,n):
                LU[i][j] = A[i][j] + x*A[k][j]

   LU = add_coluna(LU,b,n)

   return LU

######Main########

n = int(input("Digite o tamanho da Matriz: "))
A = criar_matriz_quadrada(n)
b = criar_vetor_b(n)

for i in range(n):
    for j in range(n):
        A[i][j] = float(input("Informe a[%i][%i]: " %(i,j)))

for i in range(n):
    b[i] = float(input("Informe b[%i]: " %i))

pivotamento = int(input("Digite 1 para usar pivotamento parcial e 0 para não usar: "))	

print("Matriz Original:")
M = add_coluna(A,b,n)
printar_matriz(M,n,n+1)

x = matrizes_LU(A,n,b,pivotamento)


print("Solução: ")
printar_vetor(x,n)
