# -*- coding: utf-8 -*-
import sys
import math
from timeit import default_timer as timer

"""
  "   Para executar este método no caso de teste no qual f(x) = x³ - 9x + 3 e a
  "   precisão vale 0.0005 (exemplo apresentado nos slides), deve-se definir os
  "   dois pontos do intervalo (0 e 1) e o número de interações (50) no ato do
  "   chamamento da função, bem como escrever a seguinte passagem no terminal:
  "   python .\secant_method.py "x**3 - 9*x + 3" 0.0005
  """

f = lambda x:eval(sys.argv[1]) # recebe a função
e = float(sys.argv[2]) # recebe a precisão

def q(x0, x1): # define a função phi(x)
    return (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))


start = timer()

def secant_method(x0, x1, max_interactions): # função que realiza as iterações
    fx0 = f(x0)
    fx1 = f(x1)

    if abs(fx0) <= e:
        return x0

    if abs(fx1) <= e:
        return x1

    else:
        k = 1
        str_k = 'k'
        str_x = 'x'
        str_fx = 'f(x)'

        print("{0:^2}".format(str_k) + "|{0:^14}".format(str_x) + "|{0:^14}".format(str_fx))

        while k <= max_interactions:
            x2 = q(x0, x1)
            fx2 = f(x2)

            print("{0:^2}".format(k) + "|{0:^14.6e}".format(x2) + "|{0:^14.6e}".format(fx2))

            if abs(fx2) <= e:
                return x2

            x0 = x1
            x1 = x2
            k += 1

        return x2


end = timer()
root = secant_method(0,1, 50) # definindo os pontos iniciais e o número máximo de iterações
print("Root: %.6e." % root)
print("Runtime: %.6e seconds." % (end - start))
