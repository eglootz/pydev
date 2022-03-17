import tkinter as tk
from tkinter.colorchooser import askcolor
import light_control as lc
import converter as cv


root = tk.Tk()
root.title('Tkinter Color Chooser')
root.geometry('300x150')


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    rgb = colors[0]
    coords = cv.rgb_to_xy(red=rgb[0], green=rgb[1], blue=rgb[2])
    lc.light(xy=coords)


tk.Button(
    root,
    text="SELECT",
    command=change_color).pack(expand=True)


root.mainloop()
