from numpy import *


def gaussSeidel(a,b,x,tol = 1.0e-9):
    omega = 1.0
    k = 10
    p = 1
    for i in range(1,501):
        xOld = x.copy()
        x = iterEqs(a,b,x,omega)
        dx = sqrt(dot(x-xOld,x-xOld))
        if dx < tol: return x,i,omega
        # Compute of relaxation factor after k+p iterations
        if i == k: dx1 = dx
        if i == k + p:
            dx2 = dx
            omega = 2.0/(1.0 + sqrt(1.0 - (dx2/dx1)**(1.0/p)))
    print ("Gauss-Seidel failed to converge")


def iterEqs(a,b,x,omega) :


    for i in range(len(x)) :
        soma = 0.0
        soma2 =0.0
        for j in range (i) :
            soma += a[i,j]*x[j]

        for j in range (i+1,len(x)) :
            soma2 += a[i][j]*x[j]

            
        x[i] = (omega/a[i,i]) *(b[i] - soma - soma2) + (1-omega)*x[i]

    return x
    


'''
O método de Gauss Seidel é um metodo iterativo para a resolução de problemas do
tipo A x = b , esse método pode ser aplicado a qualquer matriz que não tenha
zeros na diagonal principal, porém só tem resultado garantido para matrizes de
diagonal dominante ou simetrica e definida positiva, uma vez que seu resultado é
na verdade uma tentativa de se achar o resultado através de substituição ascendente
do valor de x, encontra-se esse resultado quando x converge, porém, há chances de
que isso não aconteça. Para o algoritmo de GaussSeidel a seguir é necessário que
seja passada a matriz A, o vetor B e além disto um vetor X que seria o suposto
resultado.
'''






