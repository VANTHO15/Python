from sympy import *
x, y, z, t=symbols(" x y z t")
k,m,n= symbols("k m n",integer=True)
f,g,h=symbols("f g h",cls=Function)
init_printing(use_unicode=True)

kq1=diff(2*x**2+2*x,x)  # diff  đạo hàm
print(kq1)

kq2=diff(2*x**3+3*x**2+2*x-1,x,3)  # đạo hàm cấp 3
print(kq2)

kq3=diff(2*y*x**3+3*z*x**2+2*x-2*x*y*z,x,y,z)  # đạo hàm theo từng biến
print(kq3)

f=Derivative(x**2+ln(x),x)
kq4=f.doit()
print(kq4)

