import requests

# disabling warnings (certification issue)
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# first program
light = "https://192.168.178.71/api/dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa/lights/1/state"
color = input("Enter a color: ")

if color.lower() == "green":
    data = '{"on":true, "sat":254, "bri":254,"hue":25500}'

if color.lower() == "blue":
    data = '{"on":true, "sat":254, "bri":254,"hue":46920}'

requests.put(light, data, verify=False)
