# Evans Tjabadi
# 10 October 2019
# Sensitivity

import matplotlib.pylab as plt
import numpy as np

# User Sensitivity

price = np.arange(0.5,2.001,0.0625)

sensitivity = 3.16*np.exp(-2.3*price)

plt.plot(price, sensitivity)
plt.xlabel("Price")
plt.ylabel("Sensitivity Factor")
plt.savefig("figs/sensitivity.png")
#plt.show()

# Typical Arrival rate

hours = np.arange(0,25,1)
typ_a_r = [0.04,0.04,0.04,0.04,0.04,0.04,0.1,0.2,0.3,0.5,0.6,0.8,0.6,0.45,0.6,0.62,0.68,0.5,0.4,0.4,0.3,0.2,0.08,0.08,0.08]
normalised_a_r = []

for i in typ_a_r:
    normalised_a_r.append(i*15)

plt.figure()
plt.xlabel("hours")
plt.ylabel("Arrival Rate")
plt.step(hours,normalised_a_r)
plt.savefig("figs/typical.png")
#plt.show()

# Hour price per day (parameters from price function)
mu = 0.8
tau = 3
phi = 1.1
gam = 3

a = 0.159
b = 0.7
c = 2

C = 100

day_price = []
for p in normalised_a_r:
    r = -14.3*p+114
    day_price.append(a*np.arctan(b*(p - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi)

plt.figure()
plt.step(hours, day_price)
plt.xlabel("hours")
plt.ylabel("Typical Day prices")
plt.savefig("figs/day_price.png")
#plt.show()

# ideal arrival Rate
eff_a_r = []
for j in day_price:
    eff_a_r.append(20*3.16*np.exp(-2.3*j)+1.5)

plt.figure()
plt.step(hours,eff_a_r)
plt.ylim(0,12)
plt.xlabel("hours")
plt.ylabel("Ideal Arrival Rate")
plt.savefig("figs/ideal.png")


# Effective arrival Rate

eff_a_r[0] = 0.1
eff_a_r[1] = 0.2
eff_a_r[2] = 0.2
eff_a_r[3] = 0.2
eff_a_r[4] = 0.9
eff_a_r[4] = 4.5


eff_a_r[22] = 2
eff_a_r[23] = 1.2
eff_a_r[24] = 1
plt.figure()
plt.step(hours, normalised_a_r, color="b",label = "Original")
plt.step(hours,eff_a_r,color="r", label = "Effective")

plt.legend(loc='upper right')
plt.xlabel("hours")
plt.ylabel("Arrival Rate")
plt.savefig("figs/effective.png")
plt.show()
