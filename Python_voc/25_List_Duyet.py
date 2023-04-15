lst=[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i,end=" ")
print(" ")
for i in range(len(lst)):
    print(lst[i],end=" ")
print(" ")
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")