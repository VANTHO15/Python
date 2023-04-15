import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,10)
line=plt.plot(x,np.sin(x)+np.cos(x))
plt.show()

x=np.linspace(-5,5)
#x**2+2*x+1
func=np.poly1d(np.array([1,2,1]).astype(float))
line=plt.plot(x,func(x))
plt.show()