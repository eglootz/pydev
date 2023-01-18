import completion

while True:
    eingabe = input("E: >>> ")
    prompt = eingabe
    response = completion.chat(prompt)
    string_response = completion.get_response(response)
    string_response = string_response.lstrip('\n')
    print(f"A: >>> {string_response}")