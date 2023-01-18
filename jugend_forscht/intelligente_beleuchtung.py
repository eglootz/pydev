import completion
import light_control as lc
import converter as cv


while True:
    eingabe = input("Phrase: ")
    prompt = f"Gib eine RGB-Farbe einem Tupel ausgedrückt an, welche dem Gefühl der folgenden Beschreibung zugehörig ist: \"{eingabe}\""
    response = completion.chat(prompt)
    RGB = eval(completion.get_response(response))
    coords = cv.rgb_to_xy(red=RGB[0], green=RGB[1], blue=RGB[2])
    
    lc.colored_light(xy=coords)
    print(f"Licht auf {RGB} eingestellt!")
    