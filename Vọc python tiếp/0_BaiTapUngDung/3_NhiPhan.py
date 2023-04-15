def DecToBi(n):
    if(n>1):
        DecToBi(n//2)
    print(n%2,end=" ")
n= int(input("Nhap sô: "))
DecToBi(n)

def cach2(n):
    while( n>0):
        yield n % 2
        n=n//2

Lis=cach2(n)
print(type(Lis))
for i in Lis:
    print(i,end=" ")

