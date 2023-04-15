def Tong(*data):
    t=0
    for i in data:
        t+=i
    return t
Sum=Tong(10,20,30,45)
print(Sum)

################
def Tong1(*data):
     kq=[]
     for i in data:
         T=0
         for j in i:
             T = T + j
         kq.append(T)
     return kq
tho=Tong1([1,2,3],[5,6,7],[5,4,6])
print(tho)








