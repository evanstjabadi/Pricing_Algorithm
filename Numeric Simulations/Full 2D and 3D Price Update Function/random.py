# Evans Tjabadi
# 22 September 2019
# random 50 calls and revenue


import numpy as np
import random
import matplotlib.pylab as plt

# Definition of variables
# Capacity
C = 100

# Call bandwidth
bv = 4
bi = 1

# for the slice 1
nv = 0
ni = 0

R = []
r = 0
Price = []

mu = 0.8
tau = 3
phi = 1.1
gam = 3

a = 0.159
b = 0.7
c = 2

d = np.arange(0,12,0.125) # Arrival Rate
r = -14.3*d+114           # Remaining resources


Price = a*np.arctan(b*(d - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi


print("Stochastic Data Generation")
# Make 50 random prices

prices = []
calls = np.linspace(1,50,50)
for i in range(50):
    f = random.choice(Price)
    prices.append(float(f))


plt.figure()
plt.scatter(calls,prices,c="red")
plt.xlabel("Calls")
plt.ylabel("Price")
plt.savefig("figs/random_Prices")
plt.show()


U = np.random.geometric(p=0.35, size=50)
plt.figure()
plt.scatter(calls,U,c="green")
plt.xlabel("Calls")
plt.ylabel("bbu per call")
plt.savefig("figs/random_usage")
plt.show()


# Revenue now
r0 = prices[0]*U[0]
R = [r0]
bbu = []
bbu.append(U[0])
for i in range(1,50):
    c = prices[i]*U[i]
    r1 = c + R[i-1]
    R.append(r1)

    u = bbu[i-1]+U[i]
    bbu.append(u)
plt.figure()
plt.plot(bbu,R,label='Designed')
plt.xlabel("bbu used")
plt.ylabel("Aggregate Revenue")


#plt.savefig("figs/random_revenue")

rev1 = [1,1.5,3.5,4,8,25,58,80,125,144,200]
bb = np.arange(10,111,10)
plt.plot(bb,rev1,label='PSCP')
plt.legend(loc='lower right')
plt.savefig("figs/Compare_rev")

plt.show()

