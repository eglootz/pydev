import cam

i = 0

while True:
    if input("Drück ya:") == "ya":
        cam.picture(f"{i}")
        i = i + 1
