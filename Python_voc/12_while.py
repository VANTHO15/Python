n=int(input("moi nhap số: "))
s=0;
while n!=0:
    s=s*10+n%10
    n=n//10
print(s)