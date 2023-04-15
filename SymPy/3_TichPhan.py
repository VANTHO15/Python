from sympy import *
x, y, z, t=symbols(" x y z t")
k,m,n= symbols("k m n",integer=True)
f,g,h=symbols("f g h",cls=Function)
init_printing(use_unicode=True)

kq1=integrate(x**2+2*x,x)# nguyên hàm
print(kq1)

kq2=integrate(x**2+2*x,(x,1,4))#Tích phân từ 1 đến 4
print(kq2)

f=Integral(exp(-x),(x,0,oo))  # tích phân từ 0 đến vô cùng
print(f)
kq3=f.doit()
print(kq3)

g=Integral(exp(-x**2-y**2),(x,0,oo),(y,0,oo))
kq4=g.doit()
print(kq4)