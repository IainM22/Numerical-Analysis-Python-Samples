'''
Iain McCown. Last edited 3/25/2016

The functions below are two variations of Gaussian Elimination. The first
function, GE(a) takes matrix a as a parameter and performs Gaussian elimination
to turn the matrix into an upper diagonal matrix. This is helpful for calculating
the determinant of the matrix quicker, or for solving a linear system of equations
Ax=b where A is a known nxn matrix, b is a known vector of length n and x is
an unknown vector of length n.

For solving the linear system described above, I define Gaussian(a,b) that takes
matrix a and vector b in the system Ax=b and it returns vector b. The function
does this by using Gaussian Elimination to turn matrix a into an upper triangular
matrix and then performing backwards substitution to find vector b. This function
uses the library 'numpy.'
'''


def GE(a):
    A = a.copy()
    n = len(a)
    for i in range(0,n-1):
            for j in range(i+1,n):
                    if(A[i][i] == 0):
                            m = 0
                    else:
                            m = (A[j][i])/(A[i][i])
                            A[j][i] = 0
                    for k in range(i+1,n):
                            A[j][k] = A[j][k] - m*A[i][k]
    return A



def Gaussian(a,b):
    A = a.copy()
    B = b.copy()
    n = np.size(B)
    for i in range(0,n-1):
            for j in range(i+1,n):
                    if(A[i][i] == 0):
                            m = 0
                    else:
                            m = (A[j][i])/(A[i][i])
                            A[j][i] = 0
                    for k in range(i+1,n):
                            A[j][k] = A[j][k] - m*A[i][k]
                    B[j] = B[j] - m*B[i]
    x = np.array([0.]*n)
    k = n-1
    x[k] = B[k]/A[k,k]
    while(k >= 0):
            x[k] = (B[k] - np.dot(A[k,k+1:],x[k+1:]))/A[k,k]
            k = k-1
    return x
