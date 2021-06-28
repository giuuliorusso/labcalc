import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt("out/sinxx.dat", unpack=True)

# sin(x) / x
plt.plot(x, y, label="sin(x) / x")

# Blue line
plt.plot(x, x * 0, "--b")

# Red points
plt.plot(
    [i * np.pi for i in range(-6, 7) if i != 0],
    [0 for i in range(12)],
    "or",
    label="$ x_i $"
)


plt.title("sin(x) / x")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()

plt.savefig("out/sinxx")
plt.show()
