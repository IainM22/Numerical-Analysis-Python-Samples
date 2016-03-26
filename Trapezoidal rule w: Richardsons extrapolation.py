'''
Iain McCown. Last edited 3/25/2016

The function Trapezoidal(a,b,n,f) uses the composite trapezoidal rule to
integrate the function 'f' between 'a' and 'b' using 'n' number of nodes.

The composite trapezoidal rule is typically second order accurate so you can
run 'Richardsons(n,f)' which performs richardsons extrapolation on the composite
trapezoidal rule, making it fourth order accurate.
'''



def Trapezoidal(a,b,n,f):
    h = (b-a)/n
    x = []
    #Create the nodes
    for i in range(n+1):
        x.append(a + i*h)
    #run the actual function
    result = 0
    for k in range(1,n+1):
        result += (h/2)*(f(x[k-1]) + f(x[k]))
    return result


def Richardsons(n,f):
    return (1/3)*(4*Trapezoidal(1,3,2*n,f) - Trapezoidal(1,3,n,f))

