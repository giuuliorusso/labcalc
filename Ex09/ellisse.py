import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(5, 5))

# Punti
x, y = np.loadtxt("ellisse.dat", unpack=True)
plt.plot(x, y)

# Ellissi
x = np.linspace(-2, 2, 1000)

y = np.sqrt(1 - x ** 2 / 4)  # Ellisse 1
plt.plot(x, y, "r", alpha=0.5)
plt.plot(x, -y, "r", alpha=0.5)

y = np.sqrt((1 - x ** 2) * 4)  # Ellisse 2
plt.plot(x, y, "r", alpha=0.5)
plt.plot(x, -y, "r", alpha=0.5)


plt.title("Metodo Monte Carlo")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()

plt.savefig("ellisse")
plt.show()
