from tkinter.colorchooser import askcolor
import light_control as lc
import converter as cv


def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    rgb = colors[0]
    coords = cv.rgb_to_xy(red=rgb[0], green=rgb[1], blue=rgb[2])
    lc.light(xy=coords)
