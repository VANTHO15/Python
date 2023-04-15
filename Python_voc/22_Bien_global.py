
def doicho():
    global a
    global b
    tg=a
    a=b
    b=tg
a,b=eval(input("nhap a,b "))
doicho()
print(a,b)
