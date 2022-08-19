import requests

light = "http://192.168.178.71/api/JoSOxXkKb6sVDmTNEVsGel3sFh0wehyC3WHv0oAv/lights/1/state"
color = input("Enter a color: ")

if color == "green":
    data = '{"on":true, "sat":254, "bri":254,"hue":25500}'

if color == "blue":
    data = '{"on":true, "sat":254, "bri":254,"hue":46920}'

requests.put(light, data)
