# McKenna Branting
# Project 7 Part 1
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz parameters and initial conditions
sigma = int(input("Enter a sigma value: "))
beta = float(input("Enter a beta value: "))
rho = int(input("Enter a rho value: "))

u0 = float(input("Enter a u0 value: "))
v0 = float(input("Enter a v0 value: "))
w0 = float(input("Enter a w0 value: "))

# u0, v0, w0 = 0, 1, 1.05

# Maximum time point and total number of time points
# tMax, n = 100, 10000

tMax = int(input("Enter a max time point value: "))
n = int(input("Enter the total number of time points: "))


def lorenz(X, t, sigma, beta, rho):
    """The Lorenz equations."""
    u, v, w = X
    up = -sigma * (u - v)
    vp = rho * u - v - u * w
    wp = -beta * w + u * v
    return up, vp, wp


# Integrate the Lorenz equations on the time grid t
t = np.linspace(0, tMax, n)
f = odeint(lorenz, (u0, v0, w0), t, args=(sigma, beta, rho))
x, y, z = f.T

# Plot the Lorenz attractor using a Matplotlib 3D projection
fig = plt.figure()
ax = fig.gca(projection='3d')

# Make the line multi-coloured by plotting it in segments of length s which
# change in colour across the whole time series.
s = 10
c = np.linspace(0, 1, n)
for i in range(0, n - s, s):
    ax.plot(x[i:i + s + 1], y[i:i + s + 1], z[i:i + s + 1], color=(1, c[i], 0), alpha=0.4)

# Remove all the axis clutter, leaving just the curve.
ax.set_axis_off()

plt.show()

# This will graph the x(t) graphs
plt.title("x(t)")
plt.xlabel("T")
plt.ylabel("X")
plt.plot(t, x)
plt.show()
# This will graph the y(t) graphs
plt.title("y(t)")
plt.xlabel("T")
plt.ylabel("Y")
plt.plot(t, y)
plt.show()
# This will graph the z(t) graphs
plt.title("z(t)")
plt.xlabel("T")
plt.ylabel("Z")
plt.plot(t, z)
plt.show()
