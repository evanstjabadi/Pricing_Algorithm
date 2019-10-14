# Evans Tjabadi
# 24 September 2019
# Comparsion to Linear Methods

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

d = np.arange(0,13,0.125) # Arrival Rate
r = -14.3*d+114           # Remaining resources
#r = 0

Price = a*np.arctan(b*(d - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi


plt.xlabel('Arrival Rate')
plt.ylabel('Price')

plt.plot(d,Price, label='Designed Scheme')
#plt.savefig("figs/Sliced_Price.png")


flat_rate = 1.4 + d*0 # Constant
plt.plot(d,flat_rate,label='flat rate')

#plt.savefig("figs/flat.png")

a = 1/25# The gradient
fixed_rate = a*d + 1

plt.plot(d,fixed_rate,label="fixed rate")
plt.legend(loc='lower right')
plt.savefig("figs/linear.png")
plt.show()
