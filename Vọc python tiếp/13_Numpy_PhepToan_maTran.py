import numpy as np
a=np.array([[1,2,3,4],[5,6,7,8]])
print(a+5)

# đôi cột trành dòng
b=np.arange(20).reshape(4,5)
print(b)
print(b.T)

c=a.copy()
print(c)