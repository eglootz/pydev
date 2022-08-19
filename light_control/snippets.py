# importing requests for communicating with the API
import requests
# importing urllib3 for disabling warnings
#import urllib3

# disabling warnings (certification issue)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# setting the username and IP-adress
user = "dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa"
ip_adress = "192.168.178.71"

# putting all lights in a list
light_states = [
    f"http://{ip_adress}/api/{user}/lights/1/state",
    f"http://{ip_adress}/api/{user}/lights/2/state",
    f"http://{ip_adress}/api/{user}/lights/3/state",
    f"http://{ip_adress}/api/{user}/lights/4/state"
]


def put_lights(data):
    # put every light in the list to the specified data (changing color, turning on/off, etc.)
    for light in light_states:
        requests.put(light, data)  # , verify=False)


# "on":bool -> turn the lights on  or off
# "sat":xxx -> specifieing the saturation
# "bri":xxx -> specifieing the brightness
# "hue": xx -> setting a color using the wierd numbers
# "xy":[x,y] -> setting a color using coordinates


def toggle(state):
    if state == "on":
        data = '{"on": true}'
    elif state == "off":
        data = '{"on": false}'
    put_lights(data=data)


# ANDERS ALS IN
def light(color):
    if color == "red":
        # setting data for the specified color
        data = '{"hue":65280}'
    elif color == "yellow":
        data = '{"hue":12750}'
    elif color == "green":
        data = '{"hue":25500}'
    elif color == "blue":
        data = '{"hue":46920}'
    elif color == "pink":
        data = '{"hue":56100}'
    elif color == "white":
        data = '{"xy":[0.4023,0.4267]}'

    put_lights(data=data)


def colored_light(xy):
    data = '{"xy":' + f"{xy}" + "}"
    put_lights(data=data)


def brightness(value):
    data = '{"bri":' + f"{value}" + "}"
    put_lights(data=data)


def saturation(value):
    data = '{"sat":' + f"{value}" + "}"
    put_lights(data=data)


# light_gui.py
# NEU, NICHT DOKUMENTIERT


def bri_slider_changed(event):
    bri = int(bri_slider.get())
    print(bri)
    lc.brightness(value=bri)


bri_slider = ttk.Scale(
    root,
    from_=0,
    to=254,
    orient='horizontal',  # vertical
    command=bri_slider_changed
    # variable=current_value
)

bri_slider.grid(
    column=3,
    row=2,
    sticky='we'
)


def sat_slider_changed(event):
    sat = int(sat_slider.get())
    print(sat)
    lc.saturation(value=sat)


sat_slider = ttk.Scale(
    root,
    from_=0,
    to=254,
    orient='horizontal',  # vertical
    command=sat_slider_changed
)

sat_slider.grid(
    column=4,
    row=2,
    sticky='we'
)
