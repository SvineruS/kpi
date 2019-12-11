import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import numpy as np


def f(x):
    return np.tan(x) / x


x = np.linspace(-5, 5, 100)
y = f(x)


root = tkinter.Tk()
root.wm_title("Lab3")

fig = Figure()
fig.add_subplot().plot(x, y)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

toolbar = NavigationToolbar2Tk(canvas, root)
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

button = tkinter.Button(master=toolbar, text="Пососать минет", command=lambda: root.quit())
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
