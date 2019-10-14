# Evans Tjabadi
# 22 September 2019
# Effect of Remaining resources on the price

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
mu = 0.8
tau = 3
phi = 0.9

fig = plt.figure(1)
ax = fig.gca(projection='3d')

# Make data.
nv = np.arange(0, int((0.4*C)/bv), 1)
ni = np.arange(0, int((0.6*C)/bi), 1)
nv, ni = np.meshgrid(nv, ni)
R = C-nv*bv-ni*bi
Price = mu*np.exp(-tau*(R/C))+phi

# Plot the surface.
#surf = ax.plot_surface(nv, ni, Price, cmap=cm.coolwarm,
                      # linewidth=0, antialiased=False)
surf = ax.plot_surface(nv, ni, Price, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_xlabel('Admitted Video Calls (nv)')
ax.set_ylabel('Admitted Instant Messaging calls (ni)')
ax.set_zlabel('Price per bbu')
#ax.set_title("The Price of resources with allocated calls")

plt.savefig("figs/Price_RM_effect.png")
plt.show()

# The second plot
fig = plt.figure()
ax = fig.gca(projection='3d')
nv = np.arange(0, int((0.4*C)/bv), 1)
ni = np.arange(0, int((0.6*C)/bi), 1)
nv, ni = np.meshgrid(nv, ni)
R = C-nv*bv-ni*bi
surf = ax.plot_surface(nv, ni, R, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_xlabel('Admitted Video Calls (nv)')
ax.set_ylabel('Admitted Instant Messaging calls (ni)')
ax.set_zlabel('Remaining Avail Capacity')


plt.savefig("figs/Remaining_Resources_3D.png")
plt.show()
