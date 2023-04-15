def tang():
    Lis=[]
    for i in range(1,10,1):
        if(i%2==0):
            yield i
LisTho=tang()
for i in LisTho:
    print(i)