def Tong(x1,x2,*data,**Dic):
    T1=0
    T2=0
    T3=0
    T1=x1+x2
    for i in data:
        T2+=i
    for k,v in Dic.items():
        T3+=v
    Lis=[T1,T2,T3]
    return Lis
LisTho=Tong(1,2,10,20,Tho=10,A=30,B=50)
print(LisTho)
