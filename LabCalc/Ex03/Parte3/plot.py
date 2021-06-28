import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt("out/zero2.dat", unpack=True)
plt.plot(x, y, "-o")

plt.title("sin(x) / x")
plt.xlabel("Numero intervalli")
plt.ylabel("Numero zeri")
plt.grid()

plt.savefig("out/zero2")
plt.show()
