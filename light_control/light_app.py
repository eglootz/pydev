# import the tkinter module for gui
import tkinter as tk
from tkinter import ttk
# importing other files and functions from this directory
import light_control as lc
import check_motion as cm
# importing urllib3 for disabling warnings
import urllib3
# importing the time module for logging motion times
import time
# import the camera function
import cam

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


red_button = ttk.Button(root, text="RED", command=lambda: lc.red_light())
red_button.grid(column=0, row=1, padx=5, pady=5)

green_button = ttk.Button(root, text="GREEN", command=lambda: lc.green_light())
green_button.grid(column=1, row=1, padx=5, pady=5)

yellow_button = ttk.Button(
    root, text="YELLOW", command=lambda: lc.yellow_light())
yellow_button.grid(column=2, row=1, padx=5, pady=5)

pink_button = ttk.Button(root, text="PINK", command=lambda: lc.pink_light())
pink_button.grid(column=3, row=1, padx=5, pady=5)

blue_button = ttk.Button(root, text="BLUE", command=lambda: lc.blue_light())
blue_button.grid(column=4, row=1, padx=5, pady=5)

white_button = ttk.Button(root, text="WHITE", command=lambda: lc.white_light())
white_button.grid(column=5, row=1, padx=5, pady=5)

on_button = ttk.Button(root, text="ON", command=lambda: lc.turn_on())
on_button.grid(column=0, row=2, padx=5, pady=5)

off_button = ttk.Button(root, text="OFF", command=lambda: lc.turn_off())
off_button.grid(column=1, row=2, padx=5, pady=5)

current_motion = False

while True:
    motion = cm.check_motion()

    if motion == True and current_motion == False:
        print(f"Motion detected: {time.strftime('%H:%M:%S')}")
        lc.red_light()
        cam.picture(name=f"{time.strftime('%H:%M:%S')}")
        current_motion = True
    if motion == False:
        current_motion = False
        lc.white_light()


root.mainloop()
