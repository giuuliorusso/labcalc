import matplotlib.pyplot as plt
import numpy as np

# Bernoulli
k, y = np.loadtxt("../Parte1/out/bernoulli_12.dat", unpack=True)
plt.plot(k, y, "-sr", label="Bernoulli")

# 100k
k, y = np.loadtxt("out/istogramma_100k.dat", unpack=True)
plt.bar(k, y, color="tab:blue", label="100k lanci")

# 50
k, y = np.loadtxt("out/istogramma_50.dat", unpack=True)
plt.bar(k, y, color="tab:green", alpha=0.5, label="50 lanci")


plt.title("nDadi = 12")
plt.xlabel("k")
plt.ylabel("f(k)")
plt.legend()
plt.grid()

plt.savefig("out/istogramma")
plt.show()
