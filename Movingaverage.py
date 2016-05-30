import numpy as np
import matplotlib.pylab as pl
def movingavg(a,n=2):
    movavg=np.cumsum(a, dtype=float)
    movavg[n:]=movavg[n:]-movavg[:-n]
    A=a
    B=movavg[n-1:]/n
    C=movavg[n-1:]/4
    a=np.sin(A)
    b=np.sin(B)
    c=np.sin(C)
    pl.figure()
    pl.plot(a)
    pl.plot(b)
    pl.plot(c)
    pl.show()
    return A,B,C
    
A=[5,7,9,11,13,15,17,19,21,23,25]
