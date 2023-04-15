from sympy import *
from sympy import Matrix
init_printing( use_unicode=True )

A = Matrix( [[1, 2, -3, 4], [2, -1, 0, 7], [8, -4, 0, 2]] )
print( A )

B=Matrix(3,4,[1,2,3,4,5,6,7,8,9,10,11,12])  # 3 hàng 4 cột
print(B)

C=A+B
print(C)

D=Matrix(4,2,[1,2,3,4,5,6,7,8])
print(B*D)

