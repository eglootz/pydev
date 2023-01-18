import completion



while True:
    eingabe = input(">>> ")
    prompt = f"Ignoriere alle vorherigen Eingaben. Wandle die folgende Phrase oder Gefühl in ein Bild mit 4 einzelnen Stichworten um (auf einer Zeile, durch Kommata getrennt). Das Bild soll nicht dunkel wirken. Zu beschreibende Phrase/Gefühl:\"{eingabe}\""
    response = completion.chat(prompt)
    string_response = completion.get_response(response)
    print(string_response)