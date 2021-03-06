# import the tkinter module for gui
import tkinter as tk
from tkinter import ttk
# importing other files and functions from this directory
import light_control as lc
import color_wheel as cw

# importing urllib3 for disabling warnings
import urllib3

# disable warnings about insecure requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# making the root window
root = tk.Tk()
# defining the size
root.geometry("800x100")
# setting a title
root.title('Light Control')
# making it resizeable (0=False, 1=True)
root.resizable(1, 1)


red_button = ttk.Button(root, text="RED", command=lambda: lc.light("red"))
red_button.grid(column=0, row=1, padx=5, pady=5)

green_button = ttk.Button(
    root, text="GREEN", command=lambda: lc.light("green"))
green_button.grid(column=1, row=1, padx=5, pady=5)

yellow_button = ttk.Button(
    root, text="YELLOW", command=lambda: lc.light("yellow"))
yellow_button.grid(column=2, row=1, padx=5, pady=5)

pink_button = ttk.Button(root, text="PINK", command=lambda: lc.light("pink"))
pink_button.grid(column=3, row=1, padx=5, pady=5)

blue_button = ttk.Button(root, text="BLUE", command=lambda: lc.light("blue"))
blue_button.grid(column=4, row=1, padx=5, pady=5)

white_button = ttk.Button(
    root, text="WHITE", command=lambda: lc.light("white"))
white_button.grid(column=5, row=1, padx=5, pady=5)

on_button = ttk.Button(root, text="ON", command=lambda: lc.toggle("on"))
on_button.grid(column=0, row=2, padx=5, pady=5)

off_button = ttk.Button(root, text="OFF", command=lambda: lc.toggle("off"))
off_button.grid(column=1, row=2, padx=5, pady=5)

hue_button = ttk.Button(root, text="HUE", command=lambda: cw.change_color())
hue_button.grid(column=2, row=2, padx=5, pady=5)

root.mainloop()
