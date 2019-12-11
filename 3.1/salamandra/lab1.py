# імпорт необхідних пакетів
import matplotlib.pyplot as plt
import numpy as np


# задана функція, записана використовуючи синтаксис Python та методи NumPy
def f(x):
    return np.tan(x) / x


# x - множина чисел від -5 до 5 з кроком 0.1 - аргументи функції
x = np.arange(-5, 5, 0.1)
# y = множина значень функції
y = f(x)

# малює ламану лінію по координатам х та у
plt.plot(x, y)
#  відображає малюнок
plt.show()
