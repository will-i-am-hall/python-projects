from tkinter import *
import matplotlib as mat
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import numpy as np


root = Tk()
root.title("Damped Oscillation Demo")
sliders = Frame(root, padx = 25, pady = 25)
sliders.configure(bg = "#000000")

root.configure(bg = "#000000")

plt.style.use('dark_background')
fig = mat.figure.Figure(figsize=(7,6), dpi=100)

thet = np.arange(-4*np.pi, 4*np.pi, 0.001)



def tofloater(num):
    canva.get_tk_widget().configure(background='#000000')
    fig.clear()
    fig.add_subplot(111, ylim = (-10,10)).plot(thet, amp.get() * np.exp(-damp.get()*thet)*np.sin(freq.get()*thet + phase.get()) + up.get())
    canva.draw()

    
amp = Scale(sliders,from_ = -10, to = 10, resolution = 0.001, length = 420, command = tofloater)
freq = Scale(sliders,from_ = -10, to = 10, resolution = 0.001, length = 420,  command = tofloater)
phase = Scale(sliders,from_ = -10, to = 10, resolution = 0.001, length = 420, command = tofloater)
damp = Scale(sliders, from_ = -1, to = 1, resolution = 0.0001, length = 420, command = tofloater)
up = Scale(sliders, from_ = -10, to = 10, resolution = 0.0001, length = 420, command = tofloater)


alb = Label(sliders, text = "Amplitude")
flb = Label(sliders, text = "Frequency")
plb = Label(sliders, text = "Phase")
dlb = Label(sliders, text = "Damping")
ulb = Label(sliders, text = "Y Offset")
 


amp.configure(bg = "#000000", fg = "#FFFFFF")
freq.configure(bg = "#000000", fg = "#FFFFFF")
phase.configure(bg = "#000000", fg = "#FFFFFF")
damp.configure(bg = "#000000", fg = "#FFFFFF")
up.configure(bg = "#000000", fg = "#FFFFFF")

alb.configure(bg = "#000000", fg = "#FFFFFF")
flb.configure(bg = "#000000", fg = "#FFFFFF")
plb.configure(bg = "#000000", fg = "#FFFFFF")
dlb.configure(bg = "#000000", fg = "#FFFFFF")
ulb.configure(bg = "#000000", fg = "#FFFFFF")

amp.grid(row = 1, column = 0)
freq.grid(row = 1, column = 1)
phase.grid(row = 1, column = 2)
damp.grid(row = 1, column = 3)
up.grid(row = 1, column = 4)

alb.grid(row = 0, column = 0)
flb.grid(row = 0, column = 1)
plb.grid(row = 0, column = 2)
dlb.grid(row = 0, column = 3)
ulb.grid(row = 0, column = 4)

canva = FigureCanvasTkAgg(fig, master=root)
canva.get_tk_widget().configure(background='#000000')
fig.add_subplot(111).plot(thet, amp.get() * np.sin(freq.get()*thet + phase.get()))

canva.draw()
canva.get_tk_widget().grid(row=1,column=0)

title = Label(root, text = "Damped Oscillation Demo", font = "Arial 24 bold")
title.configure(bg = "#000000", fg = "#FFFFFF")
title.grid(row = 0, column = 0, columnspan = 2)

sliders.grid(row = 1, column = 1, rowspan = 2)
root.mainloop()
