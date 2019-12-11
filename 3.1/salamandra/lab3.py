# імпорт необхідних пакетів
import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import numpy as np


# задана функція, записана використовуючи синтаксис Python та методи NumPy
def f(x):
    return np.tan(x) / x


# x - множина чисел від -5 до 5 з кроком 0.1 - аргументи функції
x = np.arange(-5, 5, 0.1)
# y = множина значень функції
y = f(x)


# створення вікна tkinter
root = tkinter.Tk()
# встановити назву вікна "Lab3"
root.wm_title("Lab3")

# створити фігуру та полотно matplotlib
fig = Figure()
fig.add_subplot().plot(x, y)

# створити та розмістити віджет канвасу
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# створити та розмістити віджет панелі інструментів
toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

# створити та розмістити кнопку "Вихід" на панелі інструментів
button = tkinter.Button(master=toolbar, text="Пососать минет", command=lambda: root.quit())
button.pack(side=tkinter.BOTTOM)

# запустити цикл tkinter
tkinter.mainloop()
