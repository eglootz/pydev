import tkinter
from colorthief import ColorThief
import matplotlib.pyplot as plt
import openai as oa
import json
import requests
import time
import pyshorteners
import math
from credentials import openai_api_key

oa.api_key = (openai_api_key)

# An die API (Schnittstelle mit KI) wird Anfrage gesendet
def generieren(eingabe, anzahl, größe):
    response = oa.Image.create(prompt=f"{eingabe}", n=int(anzahl), size=größe)
    return response

# Erhaltene Antwort wird auf die Links zu den Bildern reduziert
def get_url_liste(response, anzahl):
    response_string = str(response)
    response_dic = json.loads(response_string)
    url_list = []
    for key, value in response_dic.items():
        if key == 'data':
            for i in range(anzahl):
                for key2, value2 in (value[i]).items():
                    url_list = url_list + [value2]
                    print(f"‣ Bild {i + 1} umgewandelt")
    return url_list

# Verlinkte Bilder werden runtergeladen
def save_pictures(url_list, prompt):
    i = 0
    for element in url_list:
        i = i + 1
        antwort = requests.get(element)
        if antwort.status_code:
            dateiname = f'scenery.png'
            with open(dateiname, 'wb') as fp:
                fp.write(antwort.content)

def rgb_wert(dateiname, farb):
    ct = ColorThief(dateiname)
    return ct.get_color(quality = farb)


def farbe(qualit):
    global rgb_tupel
    rgb_tupel = rgb_wert("scenery.png", farb=qualit)
    farb_label.config(text=rgb_tupel, justify="left")

def farbe2(qualit):
    global rgb_tupel2
    rgb_tupel2 = rgb_wert("scenery.png", farb=qualit)
    farb_label2.config(text=rgb_tupel2, justify="left")

def farb3(qualit):
    global rgb_tupel3
    rgb_tupel3 = rgb_wert("scenery.png", farb=qualit)
    farb_label3.config(text=rgb_tupel3, justify="left")



def brightness():
    global helligkeit
    helligkeit = get_luminance(rgb_tupel)
    helligkeits_label.config(text=helligkeit, justify="left")

def machen():
    global name_entry
    response = generieren(eingabe=name_entry.get(), anzahl=1, größe="1024x1024")
    url_list = get_url_liste(response=response, anzahl=1)
    save_pictures(url_list=url_list, prompt=name_entry.get())

    farbe(qualit=1)
    change_color()
    farbe2(qualit=2)
    change_color2()
    farb3(qualit=3)
    change_color3()
    

def get_luminance(tuple):
    R = int(tuple[0])
    G = int(tuple[1])
    B = int(tuple[2])
    luminance = math.sqrt(0.299*R*R + 0.587*G*B + 0.114*B*B)
    return luminance

def change_color():
    rgb_label.config(bg=rgb_to_hex(rgb_tupel), justify="left")

def change_color2():
    rgb_label2.config(bg=rgb_to_hex(rgb_tupel2), justify="left")

def change_color3():
    rgb_label3.config(bg=rgb_to_hex(rgb_tupel3), justify="left")


def rgb_to_hex(rgb):
    r, g, b = rgb
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)



# Initialisieren GUI
main = tkinter.Tk() #Erstellen der GUI
main.geometry("480x500") #Festlegung der Maße
main.title('Lichtersteuerung') #Titel
main.resizable(1, 1) #Man kann manuell die Größe des Fensters ändern


#Startknopf (BEFEHL)
start_button = tkinter.Button(main, text="Start", command=lambda: machen())
start_button.grid(row=0, column=0, sticky=tkinter.EW)
name_entry = tkinter.Entry(main)
name_entry.insert(0, "Szene eingeben")
name_entry.grid(row=1, column=0, sticky=tkinter.EW)
farb_label = tkinter.Label(text="")
farb_label.grid(row=2, column=0)
farb_label2 = tkinter.Label(text="")
farb_label2.grid(row=3, column=0)
farb_label3 = tkinter.Label(text="")
farb_label3.grid(row=4, column=0)




helligkeits_label = tkinter.Label(text="")
helligkeits_label.grid(row=5, column=0)
rgb_label = tkinter.Label(text="              ")
rgb_label.grid(row=6, column=0)
rgb_label2 = tkinter.Label(text="              ")
rgb_label2.grid(row=7, column=0)
rgb_label3 = tkinter.Label(text="              ")
rgb_label3.grid(row=8, column=0)




# PROGRAMM LÄUFT
main.mainloop()