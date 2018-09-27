# -*- coding: utf-8 -*-
import sys

def ponto_fixo(f, fit, x0, epsilon, maxIter=50):
    ## Teste para saber se x0 é raiz
    if abs(f(x0)) < epsilon:
        return x0

    ## Mostra na tela cabeçalho da tabela
    print("k\t  x\t\t  f(x)\t\t")

    k = 1
    while k <= maxIter:
        x1 = fit(x0)
        ## Mostra valores na tela
        print("%d\t%e\t%e\t" % (k, x1, f(x1)))
        ## Caso de parada
        if abs(f(x1)) < epsilon:
            print("x = %e e f(x) = %e" % (x1, f(x1)))
            return x1
        x0 = x1
        k += 1

    print("ERRO! número máximo de iterações atingido.")

f = lambda x: eval(sys.argv[1])
fit = lambda x: eval(sys.argv[2])
x0 = float(sys.argv[3])
epsilon = float(sys.argv[4])

ponto_fixo(f, fit, x0, epsilon)
