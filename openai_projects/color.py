from colorthief import ColorThief
import matplotlib.pyplot as plt

def rgb_wert(dateiname):
    ct = ColorThief(dateiname)
    return ct.get_color(quality = 1)