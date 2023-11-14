import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(1000,dtype='float')
u = np.zeros(1000,dtype='float')
t = np.zeros(1000)

a = 7**5
c = 0
m = (2**31)-1

x[0] = 1
u[0] = x[0]/m

for i in range(1,1000):
  x[i] = (a*x[i-1]+c)%m
  u[i] = x[i]/m

print(u)

for i in range(0,1000):
  t[i] = i

plt.plot(t,u,'o')
plt.show()


