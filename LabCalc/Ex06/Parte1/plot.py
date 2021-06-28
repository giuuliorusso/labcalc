import matplotlib.pyplot as plt
import numpy as np

ns = [2, 4, 8, 12]
colors = ["tab:blue", "tab:green", "tab:red", "tab:orange"]

for n, c in zip(ns, colors):
    filename = f"out/bernoulli_{n}"

    k, y = np.loadtxt(f"{filename}.dat", unpack=True)
    plt.figure()
    plt.bar(k, y, color=c)

    plt.title(f"n = {n}")
    plt.xlabel("k")
    plt.ylabel("P(k)")
    plt.savefig(filename)

plt.show()
