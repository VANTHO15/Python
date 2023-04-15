def GT(n):
    if(n==0 or n==1):
        return 1
    else:
        return GT(n-1)*n

n= int(input("Moi nhap 1 so: "))
print("{0}!={1}".format(n,GT(n)))
