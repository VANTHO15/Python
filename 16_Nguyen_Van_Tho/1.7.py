s= input("Moi nhap chuoi : ")
a=[0]*100
for i in range(0,len(s),1):
   a[i]=ord(s[i])
for i in range(0,len(s)-1,1):
    for j in range(i+1,len(s),1):
        if(a[i]>a[j]):
            tg=a[i]
            a[i]=a[j]
            a[j]=tg
for i in range(0,len(s),1):
    print(chr(a[i]))

       