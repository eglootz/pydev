# importing requests for communicating with the API
import requests

import time

from credentials import ip_adress, user


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
        # time.sleep(1)
        requests.put(light, data)  # , verify=False)  # , timeout=3)


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


def light(color):
    if color == "red":
        # setting data for the specified color
        data = '{"on":true, "sat":254, "bri":254,"hue":65280}'
    elif color == "yellow":
        data = '{"on":true, "sat":254, "bri":254,"hue":12750}'
    elif color == "green":
        data = '{"on":true, "sat":254, "bri":254,"hue":25500}'
    elif color == "blue":
        data = '{"on":true, "sat":254, "bri":254,"hue":46920}'
    elif color == "pink":
        data = '{"on":true, "sat":254, "bri":254,"hue":56100}'
    elif color == "white":
        data = '{"on":true, "sat":254, "bri":254,"xy":[0.4023,0.4267]}'

    put_lights(data=data)


def colored_light(xy):
    data = '{"on":true, "sat":254, "bri":254,"xy":' + f"{xy}" + "}"
    put_lights(data=data)


def brightness(value):
    data = '{"bri":' + f"{value}" + "}"
    put_lights(data=data)


def saturation(value):
    data = '{"sat":' + f"{value}" + "}"
    put_lights(data=data)
