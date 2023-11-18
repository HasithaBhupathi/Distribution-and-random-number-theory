import numpy as np
import matplotlib.pyplot as plt

x = np.zeros(1001,dtype='float')
u = np.zeros(1000,dtype='float')
t = np.zeros(1000)
a = 7**5


m = (2**31)-1
k = 5
b = 1
c = 0
N = 1000

x[0] = 1

for i in range(1,k):
  x[i] = (b*x[i-1]+c)%m
  u[i-1] = x[i]/m

for i in range(k,N+1):
  s = 0
  for r in range(1,k+1):
    s = s+a*x[i-r]
  x[i] = s%m
  u[i-1] = x[i]/m

for i in range(0,1000):
  t[i] = i

print(u)

plt.plot(t,u,'o')
plt.show()
