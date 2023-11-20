import numpy as np
import matplotlib.pyplot as plt

N = 1000

x = np.zeros(N+1,dtype='float')
y = np.zeros(N+1,dtype='float')
z = np.zeros(N+1,dtype='float')
r = np.zeros(N+1,dtype='float')
u = np.zeros(N,dtype='float')
t = np.zeros(N)

m = ([30269,30307,30323,30347])
x[0] = 1
y[0] = 2
z[0] = 3
r[0] = 4

for i in range(1,N+1):
   x[i] = (171*x[i-1])%m[0]
   y[i] = (172*y[i-1])%m[1]
   z[i] = (170*z[i-1])%m[2]
   r[i] = (173*r[i-1])%m[3]
 
   u[i-1] = (x[i-1]/m[0]+y[i-1]/m[1]+z[i-1]/m[2]+r[i-1]/m[3])%1

for i in range(0,N):
  t[i] = i

print(u)

plt.plot(t,u,'o')
plt.show()


