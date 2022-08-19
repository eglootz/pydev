import requests

# advanced program
urls = [
    "http://192.168.178.71/api/dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa/lights/1/state",
    "http://192.168.178.71/api/dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa/lights/2/state",
    "http://192.168.178.71/api/dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa/lights/3/state",
    "http://192.168.178.71/api/dCOuv5NAZaNSuZ5UGbB7dHEUfB182FjhMbPateTa/lights/4/state"
]

print("Starting the program.")

print("Turn lights on/off")

state = input()

if state.lower() == "on":
    data = '{"on": true}'
if state.lower() == "off":
    data = '{"on": false}'

for light in urls:
    requests.put(light, data)


if state.lower() == "on":

    print("Do you want to change the color? (y/n)")
    answer = input()
    if answer.lower() == "y":

        print("Please enter a valid color:")
        color = input()
        if color.lower() == "yellow":
            data = '{"on":true, "sat":254, "bri":254,"hue":12750}'

        elif color.lower() == "green":
            data = '{"on":true, "sat":254, "bri":254,"hue":25500}'

        elif color.lower() == "blue":
            data = '{"on":true, "sat":254, "bri":254,"hue":46920}'

        elif color.lower() == "pink":
            data = '{"on":true, "sat":254, "bri":254,"hue":56100}'

        elif color.lower() == "red":
            data = '{"on":true, "sat":254, "bri":254,"hue":65280}'

        else:
            print("Color currently not available.")

        for light in urls:
            requests.put(light, data)  # , verify=False)

print("Sucess.")
