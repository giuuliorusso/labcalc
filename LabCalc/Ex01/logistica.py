import matplotlib.pyplot as plt
import numpy as np

# Punti
x, y = np.loadtxt("punti.dat", unpack=True)
plt.plot(x, y, "o")

# Funzione logistica
P = 20
t0 = 10
t = np.linspace(-29, 40, 200)

f = lambda k: P / (1 + np.exp(-k * (t - t0)))

k = 0.25
plt.plot(t, f(k), label="k = 1 / 4")

k = 0.5
plt.plot(t, f(k), label="k = 1 / 2")


plt.title("Curva logistica")
plt.xlabel("t")
plt.ylabel("f(t)")
plt.legend()

plt.savefig("logistica")
plt.show()
