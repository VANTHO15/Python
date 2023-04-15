from __future__ import division
from sympy import *
x, y, z, t=symbols(" x y z t")
kq=solve(2*x-1,x)
print(kq)

kq2=solve((x+5*y-2,-3*x+6*y-15),x,y)
print(kq2)

kq3=solve(sin(x)+sin(y)-1)
print(kq3)