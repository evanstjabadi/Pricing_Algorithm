# Evans Tjabadi
# 22 September 2019
# Effect of arrival rate alone

import matplotlib.pylab as plt
import numpy as np
import random
from random import gauss


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

mu = 0.4
tau = 3
phi = 1.1
gam = 3

a = 0.159
b = 0.7
c = 2

d = np.arange(0,13,0.125)
r = -14.3*d+114
#r = 0

Price = a*np.arctan(b*(d - c))+ phi

print(min(Price), max(Price))

plt.xlabel('Arrival Rate')
plt.ylabel('Price per bbu')
#plt.ylim(0, 2)

plt.plot(d,Price)
#plt.grid()

plt.savefig("figs/demand_effect.png")
plt.show()
