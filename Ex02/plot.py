import matplotlib.pyplot as plt
import numpy as np

t, x, y = np.loadtxt("out/traiettoria.dat", skiprows=1, unpack=True)

# Traiettoria
plt.figure(figsize=(5, 5))
plt.plot(x, y, "-o", color="tab:blue", markersize=3)

plt.title("Traiettoria")
plt.xlabel("x(t)")
plt.ylabel("y(t)")
plt.savefig("out/traiettoria")

# x
plt.figure(figsize=(5, 5))
plt.plot(t, x, "-o", color="tab:green", markersize=3)

plt.title("x")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.savefig("out/x")

# y
plt.figure(figsize=(5, 5))
plt.plot(t, y, "-o", color="tab:red", markersize=3)

plt.title("y")
plt.xlabel("t")
plt.ylabel("y(t)")
plt.savefig("out/y")


plt.show()
