import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(1001,dtype='float')
u = np.zeros(1000,dtype='float')
t = np.zeros(1000)

a = 7**5
c = 0
m = (2**31)-1
N = 1000

x[0] = 1

for i in range(0,N):
  x[i+1] = (a*x[i]+c)%m
  u[i] = x[i+1]/m

print(u)

for i in range(0,N):
  t[i] = i

plt.plot(t,u,'o')
plt.show()


