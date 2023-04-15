import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# # Ve diem trong khong gian
# x = [1, 3, 5, 7, 2, -1, -5, 0, 1, -9]
# y = [5, 6, -4, 12, 6, -1, 2, 10, 1, 1]
# z = [1, 4, 5, -10, 4, 7, 9, 2, -11, -2]
#
# ax.plot(x, y, z, 'o')
# plt.show()

#Ve duong thang trong khong gian
# t = np.linspace(0, 10)
# x = 2 + 3*t
# y = -1 + 2*t
# z = t
#
# ax.plot(x, y, z)
# plt.show()

# vẽ mp 2x+3y-4z-5=0
x=np.linspace(-5,5)
y=np.linspace(-5,5)
x,y=np.meshgrid(x,y)
z=(2*x+3*y-5)/4
ax.plot_surface(x, y, z)

plt.show()
