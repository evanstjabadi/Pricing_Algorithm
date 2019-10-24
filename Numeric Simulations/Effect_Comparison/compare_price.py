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

d = [0,1,2,3,4,5,6,7] # Arrival Rate
Price_P = []

for e in d:
    r = -14.3*e+114      # Remaining resources
    P = a*np.arctan(b*(e - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi
    Price_P.append(P)



plt.xlabel('Arrival Rate')
plt.ylabel('Price')


plt.plot(d,Price_P,label="Designed")
#plt.savefig("figs/Sliced_Price.png")

compare1 = [0.735,0.75,0.765,0.78,0.79,0.8,0.81,0.82]
compare_p = []

for i in compare1:
    compare_p.append(i+0.3)

plt.plot(d,compare_p,label="Comparison 1")
plt.legend(loc='lower right')
plt.savefig("figs/compare_literature1.png")
plt.show()
