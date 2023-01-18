# App: Terminal öffnen
# zum richtigen Ordner navigieren (kann variieren): 
# - cd desktop
# - cd open_ai
# Bei Bedarf: Dateien auflisten
# - ls
# Vor erstmaligem Ausführen Module installieren:
# - pip install openai
# - pip install pyshorteners
# Datei ausführen: 
# - python3.11 main.py

# Sonstige Terminal-Befehle (die du eigentlich nicht brauchst): 
# - cd .. -> geht in den übergeordneten Ordner 
# - mkdir ordnername -> erstellt Ordner
# - mv datei_alt datei_neu -> benennt um oder bewegt zu neuem Pfad
# - rm datei -> löscht Datei

# importieren der Module (vorprogrammierte Funktionen)
import openai as oa
import json
import requests
import time
import pyshorteners

# Authorisierung der Anfragen mittels Nutzerschlüssel
oa.api_key = ("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")

# Funktion (= zusammengefasster Codeblock, auf den man später zugreifen kann), die die aktuelle Zeit zurückgibt
def aktuelle_zeit():
  current_time = time.strftime("%Y-%m-%d %H.%M.%S")
  return current_time

# Funktion, die einen Kurzlink generiert
def short_link(long_url):
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url)
    return short_url

# An die API (Schnittstelle mit KI) wird Anfrage gesendet
def generieren(eingabe, anzahl, größe):
    response = oa.Image.create(prompt=f"{eingabe}", n=int(anzahl), size=größe)
    return response

# Erhaltene Antwort wird auf die Links zu den Bildern reduziert
def get_url_liste(response, anzahl):
    response_string = str(response)
    response_dic = json.loads(response_string)
    url_list = []
    for key, value in response_dic.items():
        if key == 'data':
            for i in range(anzahl):
                for key2, value2 in (value[i]).items():
                    url_list = url_list + [value2]
                    print(f"‣ Bild {i + 1} umgewandelt")
    return url_list

# Verlinkte Bilder werden runtergeladen
def save_pictures(url_list, prompt):
    i = 0
    for element in url_list:
        i = i + 1
        antwort = requests.get(element)
        if antwort.status_code:
            dateiname = f'images/DALL·E {aktuelle_zeit()} - {prompt}.png'
            log = 'log.txt'
            with open(dateiname, 'wb') as fp:
                fp.write(antwort.content)
            shortlink = short_link(element)
            print(f"‣ Bild {i} heruntergeladen  [{shortlink}]")
            with open(log, "a") as l:
                l.write(f"{dateiname} | Downloaded from: {shortlink} [{element}]\n")
            

# Hauptprogramm, in welchem die zuvor programmierten Codeblöcke aufgerufen werden
while True:
    print("~~~~~~~~~~~~~~~~~")
    eingabe = input("Gib eine Bildidee ein: ")
    anzahl = input("Gib bitte die Anzahl an (1 - 10): ")
    print("~~~~~~~~~~~~~~~~~")
    print("Anfrage an API...")
    response = generieren(eingabe=eingabe, anzahl=anzahl, größe='1024x1024')
    print("Herausfiltern der Links...")
    url_list = get_url_liste(response, int(anzahl))
    print("Bilder herunterladen...")
    save_pictures(url_list, eingabe)
    print("Fertig!")