'''
Iain McCown. Last edited 3/25/2016.

The function below uses the conjugate gradient method to solve the linear
system of equations Ax=b. In order for the conjugate gradient method to work,
A must be a symmetric and positive definite.

The function conjugate(A,b,x0) takes parameters A and b as described in the
linear system above, and an initial guess, x0. Typically one uses the initial
guess of the zero vector.

This function uses the library numpy
'''

import numpy as np

def conjugate(A,b,x0):
    x = x0.copy()
    r_prev = b - np.dot(A,x)
    v = r_prev
    r = 1
    while(np.linalg.norm(r) > 1E-10):
        tk = np.dot(r_prev,v)/np.dot(v,np.dot(A,v))
        x = x + tk*v
        r = r_prev - tk*np.dot(A,v)
        S = np.dot(r,r)/np.dot(r_prev,r_prev)
        v = r + S*v
        r_prev = r.copy()
    return x
