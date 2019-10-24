# Evans Tjabadi
# 22 September 2019
# Price Comparison to Exponential

import numpy as np
import matplotlib.pylab as plt

d = np.arange(0,8,1)
e =1.25 - 0.02*np.exp(-(d-3))
mu = 0.8
tau = 3
phi = 1.1
gam = 3

a = 0.159
b = 0.7
c = 2
C = 100


r = -14.3*d+114
P = a*np.arctan(b*(d - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi

plt.plot(d,e,label="Exponential")

plt.plot(d,P,label="Designed")
plt.legend(loc='lower right')
plt.xlabel('Arrival Rate')
plt.ylabel('Price')

plt.savefig("figs/compare_literature2.png")
plt.show()
