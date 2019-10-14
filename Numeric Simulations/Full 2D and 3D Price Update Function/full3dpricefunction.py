# Evans Tjabadi
# 22 September 2019
# Full Price Update Function 3D

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import matplotlib.pylab as plt2d


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

mu = 3 # Only change here
tau = 3
phi = 1.1
gam = 3

a = 0.159
b = 0.7
c = 2

fig = plt.figure(1)
ax = fig.gca(projection='3d')

# Make data.
nv = np.arange(0, int((0.4*C)/bv), 1)
ni = np.arange(0, int((0.6*C)/bi), 1)
nv, ni = np.meshgrid(nv, ni)

d = np.arange(0,8,0.125) # Arrival Rate
r = np.arange(0,100,2)   # Remaining resources
d, r = np.meshgrid(d, r)
#nv, ni,d = np.meshgrid(nv, ni,d)


#Price = 0.5*(mu*np.exp(-tau*(r/C))+phi) +0.5*((0.318)*np.arctan(3*(d - 1.3)) + 1.1)
#Price = 0.4*exp(-tau(r/c1))
Price = a*np.arctan(b*(d - c)) + mu*np.exp(-tau*(r/C)-gam)+ phi

surf = ax.plot_surface(r, d, Price, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.set_xlabel('Remaining Avail. resources')
ax.set_ylabel('Arrival Rate')
ax.set_zlabel('Price')
#ax.set_title("The designed Price Update function")
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.savefig("figs/full3dpricefunction.png")
plt.show()
