'''
Iain McCown. Last edited 3/25/2016.

The following two functions are used for approximating a linear system of equations
Ax=b when A is a diagonally dominant matrix. jacobi(a,B) uses jacobi iteration
and stops iterating when the euclidean norm of x^(k+1) - x(k) is less than 10^(-5).

Seidel(a,B) works very similarly, but uses the values of x^(k+1) as they become
available, causing it to achieve the stopping criteria in about half as many
iterations. For further understanding on how Jacobi and Gauss Seidel iteration
works, you can read about them online.

Both of these functions use the numpy library


'''



import numpy as np

def jacobi(a,B):
    A = a.copy()
    b = B.copy()
    n = len(b)
    #Placeholder for x^k
    x_prev = np.zeros(n)
    #placeholder for x^(k+1)
    x = np.zeros(n)
    norm = np.linalg.norm(actual)
    #Initialize the difference to something high
    difference = 1
    #While the difference in iterations is greater than 10^(-5)...
    while(difference > 1E-5):
        for i in range(0,n):
            subs = 0.0
            for j in range(0,n):
                if(i != j):
                    subs += A[i,j]*x_prev[j]
            x[i] = (b[i] - subs)/A[i][i]
        difference = np.linalg.norm(x - x_prev)
        x_prev = x.copy()
    return x


def Gauss(a,B):
    A = a.copy()
    b = B.copy()
    n = len(b)
    #Placeholder for x^(k+1)
    x_prev = np.zeros(n)
    #Placeholder for x^(k)
    x = np.zeros(n)
    norm = np.linalg.norm(actual)
    #Initialize the difference to something high
    difference = 1
    while(difference > 1E-5):
        for i in range(0,n):
            subs = 0.0
            for j in range(0,i):
                subs += A[i,j]*x[j]
            for j in range(i+1,n):
                subs += A[i,j]*x_prev[j]
            x[i] = (b[i] - subs)/A[i][i]
        difference = np.linalg.norm(x - x_prev)
        x_prev = x.copy()
    return x



