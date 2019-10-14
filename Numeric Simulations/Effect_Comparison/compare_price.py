# Evans Tjabadi
# 22 September 2019
# Price Comparison

import matplotlib.pylab as plt
import numpy as np

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

d = np.arange(0,10,1) # Arrival Rate
r = -14.3*d+114      # Remaining resources

Price = a*np.arctan(b*(d - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi


plt.xlabel('Arrival Rate')
plt.ylabel('Price')


plt.plot(d,Price,label="Designed")
#plt.savefig("figs/Sliced_Price.png")

compare1 = [0.735,0.8,0.97, 0.985, 1, 1.01, 1.02, 1.03, 1.04,1.05]
compare_p = []
for i in compare1:
    compare_p.append(i+0.2)

plt.plot(d,compare_p,label="Comparison 1")
plt.legend(loc='lower right')
plt.savefig("figs/compare_literature1.png")
plt.show()
