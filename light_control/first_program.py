import requests
from credentials import ip_adress, user

light = f"http://{ip_adress}/api/{user}/lights/4/state"
color = input("Enter a color: ")

if color == "green":
    data = '{"on":true, "sat":254, "bri":254,"hue":25500}'

if color == "blue":
    data = '{"on":true, "sat":254, "bri":254,"hue":46920}'

requests.put(light, data)
print(f"Color changed to {color}")
