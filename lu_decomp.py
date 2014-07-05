from numpy import *

def LUdecomp(a):
    n = len(a)
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,k] = lam
    return a


def LUsolve(a,b):
    n = len(a)
    for k in range(1,n):
        b[k] = b[k] - dot(a[k,0:k],b[0:k])
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - dot(a[k,k+1:n],b[k+1:n]))/a[k,k]
    return b



'''

O metodo de decomposição LU através do metodo de Doolittle é bastante eficente
o que o torna interessante para resolver equaçoes do tipo Ax=b é a inexistencia
de restrições para usar esse metodo, a seguir temos o codigo que resolve um
problema no tipo citado anteriormente pelo método de decomposição LU de Doolittle
em duas partes, uma onde é feita as duas matriz L U a partir da matriz A, sendo
retornado apenas uma matriz com os elementos da diagonal e acima preenchidos pelos
elementos da matriz U e os elementos em baixo da diagonal sendo os elementos
da matriz L. Para a resolução de um problema no tipo Ax=b é passado para a
funcao LUsolve a matrix A onde já foi aplicada a decomposicão e o vetor b com
os elementos de x.

