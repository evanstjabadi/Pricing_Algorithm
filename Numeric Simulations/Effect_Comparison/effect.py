# Evans Tjabadi
# 24 September 2019
# Effect of varying bbu and Capacity

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

mu = 0.8
tau = 3
phi = 1.1
gam = 3

a = 0.159
b = 0.7
c = 2

d = np.arange(0,12,0.125) # Arrival Rate
r = -14.3*d+114           # Remaining resources


for C in range(60,151,30):
    #r = -(C1/7)*d+(8*C1/7)
    Price = a*np.arctan(b*(d - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi
    label = "C = "+ str(-C+210)
    label = "C = "+str(C)
    plt.plot(d,Price,label=label)


plt.xlabel('Arrival Rate')
plt.ylabel('Price')
plt.legend(loc='lower right')

plt.savefig("figs/cap_effect.png")
plt.show()


