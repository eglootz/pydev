# importing requests for communicating with the API
import requests
# importing urllib3 for disabling warnings
import urllib3

# disabling warnings (certification issue)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# setting the username and IP-adress
user = "dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa"
ip_adress = "192.168.178.71"

# putting all lights in a list
light_states = [
    f"https://{ip_adress}/api/{user}/lights/1/state",
    f"https://{ip_adress}/api/{user}/lights/2/state",
    f"https://{ip_adress}/api/{user}/lights/3/state",
    f"https://{ip_adress}/api/{user}/lights/4/state"
]


def put_lights(data):
    # put every light in the list to the specified data (changing color, turning on/off, etc.)
    for light in light_states:
        requests.put(light, data, verify=False)


# "on":bool -> turn the lights on  or off
# "sat":xxx -> specifieing the saturation
# "bri":xxx -> specifieing the brightness
# "hue": xx -> setting a color using the wierd numbers
# "xy":[x,y] -> setting a color using coordinates


def red_light():
    # setting data for the specified color
    data = '{"on":true, "sat":254, "bri":254,"hue":65280}'
    # calling a function to set all lights
    put_lights(data=data)


def yellow_light():
    data = '{"on":true, "sat":254, "bri":254,"hue":12750}'
    put_lights(data=data)


def green_light():
    data = '{"on":true, "sat":254, "bri":254,"hue":25500}'
    put_lights(data=data)


def blue_light():
    data = '{"on":true, "sat":254, "bri":254,"hue":46920}'
    put_lights(data=data)


def pink_light():
    data = '{"on":true, "sat":254, "bri":254,"hue":56100}'
    put_lights(data=data)


def white_light():
    data = '{"on":true, "sat":254, "bri":254,"xy":[0.4023,0.4267]}'
    put_lights(data=data)


def light(xy):
    data = '{"on":true, "sat":254, "bri":254,"xy":' + f"{xy}" + "}"
    put_lights(data=data)


def turn_on():
    data = '{"on": true}'
    put_lights(data=data)


def turn_off():
    data = '{"on": false}'
    put_lights(data=data)
