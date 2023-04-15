import numpy as np
import pandas as ap
from pandas import Series, DataFrame
from numpy.random import randn

s1 = Series([1, 2, 3, 4, 5])
print(s1)
s2 = Series([1, 2, 3, 4, 5],index=["A","B","C","D","E"])
print(s2)


diem= [10,9,10,9,8]
Hocsinh=["Tho","Thanh","Tài","Yến","Huỳnh"]
s3=Series(diem,index=Hocsinh)
print(s3)

s3d=s3.to_dict()
print(s3d)

s4=Series(s3d)
print(s4)
print(s3.values)
print(s3.index)

key=["a","b","c","d"]
data=[1,2,3,4]
x=Series(data,index=key)



# s5=data.reindex(key)
print(x)



