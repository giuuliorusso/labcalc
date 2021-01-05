import matplotlib.pyplot as plt
import numpy as np


def sort(x, y):
    l = list(zip(x, y))
    l.sort(key=lambda t: t[0])
    return zip(*l)


# Histo1
x, y = np.loadtxt("histo1.dat", unpack=True)
x, y = sort(x, y)
x = [str(i) for i in x]
plt.bar(x, y, color="tab:blue", label="Histo1")

# Histo2
x, y = np.loadtxt("histo2.dat", unpack=True)
x, y = sort(x, y)
x = [str(i) for i in x]
plt.bar(x, y, color="tab:green", alpha=0.5, label="Histo2")


plt.title("Esame")
plt.xticks(rotation=20)
plt.legend()
plt.grid()

plt.savefig("plot")
plt.show()
