def Tong2So(x,y):
    x+=1
    y+=2
    return x+y

a,b= eval(input("Mời nhập 2 số: "))
s= Tong2So(a, b)
print("a=",a)
print("b=",b)
print(s)