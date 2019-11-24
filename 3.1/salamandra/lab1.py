import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return np.tan(x) / x


x = np.linspace(-5, 5, 100)
y = f(x)

plt.plot(x, y)
plt.show()
