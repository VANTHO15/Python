from math import sqrt
a1=float(input("Nhap a="))
b1=float(input("nhap b="))
c1=float(input("Nhap c="))
if a1==0:
    if b1==0:
         if c1==0:
            print("Vô số nghiệm")
         else:
             print("Vô nghiệm")
    else:
        x=-c1/b1
        print("X1= {0}".format(x))
else:
    d=b1**2-4*a1*c1
    if d<0:
        print("Vô nghiệm")
    elif d==0:
        print("X1=X2= {0}".format(-b1/(2*a1)))
    else:
        x1=(-b1+sqrt(d))/(2*a1)
        x2=(-b1-sqrt(d))/(2*a1)
        print("X1= {0} ; X2= {1}".format(x1,x2))