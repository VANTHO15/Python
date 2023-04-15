import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from numpy.random import randn

diem=[10,9,7,9,10,9]
sinhvien=["Tho","tí","Tèo","Yến","Huỳnh","Dung"]
Dic={"Diem":diem,"sinhvien":sinhvien}

df=DataFrame(Dic)
print(df)


ind="A B C D E F".split()
cols="col col2 col3 clo4 col5 col6".split()
x=[]
for i in range(36):
    x.append(np.random.randint(1,100))

x=np.array(x)
x=x.reshape(6,6)
print(x)
df3= DataFrame(x,index=ind,columns=cols)
print(df3)

new_ind="A B C D E F G H K".split()
df4=df3.reindex(new_ind,fill_value= 0)
print(df4)

new_colmns="col1 col2 col3 col4 col5 col6 col7".split()
df5=df4.reindex(columns=new_colmns,fill_value=0)
print(df5)

print(df5["col5"])
print(df5.loc['C'])

# xóa dòng or cột
df5.drop("C")
df5.drop("col3",axis=1)
print(df5)

print(df5.sum())
print(df5.sum(axis=1))

print(df5.max())
print(df5.idxmax())
