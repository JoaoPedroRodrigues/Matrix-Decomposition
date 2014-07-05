from numpy import *

def LUdecomp5(d,e,f):
    n = len(d)
    for k in range(n-2):
        lam = e[k]/d[k]
        d[k+1] = d[k+1] - lam*e[k]
        e[k+1] = e[k+1] - lam*f[k]
        e[k] = lam
        lam = f[k]/d[k]
        d[k+2] = d[k+2] - lam*f[k]
        f[k] = lam
    lam = e[n-2]/d[n-2]
    d[n-1] = d[n-1] - lam*e[n-2]
    e[n-2] = lam
    return d,e,f


def LUsolve5(d,e,f,b):
    n = len(d)
    b[1] = b[1] - e[0]*b[0]
    for k in range(2,n):
        b[k] = b[k] - e[k-1]*b[k-1] - f[k-2]*b[k-2]
    b[n-1] = b[n-1]/d[n-1]
    b[n-2] = b[n-2]/d[n-2] - e[n-2]*b[n-1]
    for k in range(n-3,-1,-1):
        b[k] = b[k]/d[k] - e[k]*b[k+1] - f[k]*b[k+2]
    return b


'''
Neste algoritmo uma matriz pentadiagonal é decomposta em LU para resolução de um
problema onde A, a matriz pentadiagonal, esta num sistema de equações do tipo
A x = b , para resolver este problema através desse algoritmo a matriz pentadiagonal
A deve ser simétrica, o problema é resolvido em duas etapas, uma que decompoe
a matriz A, para resolução desse problema devem ser passados como argumento um
vetor com os elementos da diagonal principal, outro vetor com os elementos da
diagonal secundaria e um terceiro vetor com os elementos da 3 diagonal, esses
tres vetores tem seus valores alterados para a presentar a matriz LU resultante,
e, para a resolucao do problema, esses tres vetores devem ser passados, juntamente
com o vetor b, para a LUsolve5 que finalmente retorna o valor do vetor x
'''

