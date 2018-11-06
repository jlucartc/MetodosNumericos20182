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
    #:var A: Matriz quadrada
    A = []

    for i in range(0,n):

        linha = []

        for j in range(0,n):

            linha.append(0)

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

    for i in range(n):

        for j in range(m):

            if j < m-1:
                print("{:10.3e}".format(A[i][j]), end=" ")
            else:
                print(" | " + "{:10.3e}".format(A[i][j]), end=" ")


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


def pivotamento_parcial(A,n,m,k):
    '''

    :param A: Matriz
    :param n: Dimensão
    :param k: coluna do pivô
    :return: M - Matriz com pivô de maior módulo da coluna k
    '''

    linha = -1

    aux = A[k][k]

    #Procurar o maior módulo na coluna k
    for l in range(k+1,n):

        if abs(aux) < abs(A[l][k]):
            linha = l
            aux = A[l][k]

    #Caso seja necessário, fazer a troca de linhas k e l
    if linha != -1:

        for c in range(m):

            aux = A[k][c]
            A[k][c] = A[linha][c]
            A[linha][c] = aux

    return A

def para_matriz_triangular_superior(A,n,m,pp):
    M = A
    '''
    :param A: Matriz qualquer
    :param n: Número de linhas
    :param m: Número de Colunas
    :param pp: Se vai haver pivotamento parcial
    :return: M - Matriz triangular superior
    '''

    for k in range(0,m-1):

        if pp>0:
            M = pivotamento_parcial(A, n, m, k)

        for i in range(k+1, n):

            x = -(M[i][k] / M[k][k])

            M[i][k] = 0

            for j in range(k+1, m):
                M[i][j] = M[i][j] + x*M[k][j]

    return M

def resolver_triangular_superior(A,n,m):
    '''
    :param A: Matriz triangular superior
    :param n: Número de linhas
    :param m: Número de colunas (incluindo coluna de constantes)
    :return: Vetor solução
    '''

    n = n-1
    m = m-1
    x = []
    for i in range(n+1):
        x.append(0)

    x[n] = A[n][m] / A[n][n]

    for k in range(n-1,-1,-1):
        a = 0
        for j in range(k+1, n+1, 1):
           a += A[k][j]*x[j]

        x[k] = (A[k][m] - a) / A[k][k]

    return x


######Main########
n = int(input("Digite a dimensão da matriz(nxn): "))
m = n+1
M = criar_matriz_quadrada(n)
b = criar_vetor_b(n)

#Setando Matriz
for i in range(n):
    for j in range(n):
        M[i][j] = float(input("Digite o valor de M[%i][%i]: " % (i, j)))

#Setando vetor solução
for i in range(n):
    b[i] = float(input("Digite o valor de b[%i]: " % i))

pivotamento = int(input("Digite 1 para usar pivotamento parcial e 0 para não usar: "))
#Concatenando o vetor a matriz
A = add_coluna(M,b,n)

print("\n")

print("Matriz original: ")
printar_matriz(A,n,m)

#Transformando a matriz original em triangular superior
A_triangular = para_matriz_triangular_superior(A,n,m,pivotamento)

print("Matriz triangular: ")
printar_matriz(A_triangular,n,m)

#Resolvendo matriz triangular superior
x = resolver_triangular_superior(A_triangular,n,m)

print("Vetor solução: ")
printar_vetor(x,n)
