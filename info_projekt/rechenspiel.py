# Guten Morgen!! 
# Ich habe versucht, das Programm so ausführlich 
# wie möglich zu kommentieren, um einem der Sprache 
# vielleicht unbekannten Betrachter den Umgang zu 
# erleichtern. Trotzdem müsste ja alles Wichtige in
# der Dokumentation erklärt sein.
# Frohe Weihnachten und schönes Neues Jahr!

# Vorraussetzung: min. Python 7, besser Python 3.10
# Starten des Programms: terminal$ python3.10 rechenspiel.py

#~~~~~~~~~~~~ IMPORT ~~~~~~~~~~~~#
# importieren der benötigten Module
import time
import random
import operator
import tkinter
import tkinter.messagebox
import glob
from datetime import datetime 
from tkinter import font
#~~~~~~~~~~~~ IMPORT ~~~~~~~~~~~~#

#~~~~~~~~~~~~ INITIALISIEREN ~~~~~~~~~~~~#
#Festlegen der Operatoren, um später auf sie zugreifen zu können
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor
}
# Initialisieren GUI
main = tkinter.Tk() #Erstellen der GUI
main.geometry("480x500") #Festlegung der Maße
main.title('Der Kopfrechnen-Übungsmeister') #Titel
main.resizable(1, 1) #Man kann manuell die Größe des Fensters ändern
main.columnconfigure(2, minsize=200) #Spalte 3 kriegt feste Größe
font.families() #später kann ich auf Schriftarten zurückgreifen
#Initialisieren der Variablen
schwierigkeit = "nicht definiert"
schwierigkeit_gesetzt = False #anfangs noch keine schwierigkeit festgelegt
fertig_gerechnet = False # spiel noch nicht begonnen
spiel_begonnen = False # spiel noch nicht beendet
highscore_geklickt = False  # Highscore wurde noch nicht geklickt
warte_var = tkinter.IntVar() #Variablen, dessen spätere Änderung das Programm weiterführt
warte_var2 = tkinter.IntVar()
korrekt_liste = [] #Liste der korrigierenden Label
ergebnis_liste = [] #Liste der richtigen Ergebnisse
eingabe_liste = [] #Liste der eingegebenen Ergebnisse
op_liste = [] #Liste der verwendeten Operatoren
a_liste = [] #Listen der einzelnen Zahlen
b_liste = []
richtig = 0 #Anzahl richtiger Aufgaben
gültige_anzahl = True #Aufgrund der mit 5 initialisierten Anzahl
high_score = 0 #keine Punkte zu Beginn, sonst unfair
stats_runtergeladen = False #Statistiken wurden noch nicht runtergeladen (-> einmalig)
aufgaben_liste = []
#~~~~~~~~~~~~ INITIALISIEREN ~~~~~~~~~~~~#

#~~~~~~~~~~~~ KLASSEN (RECORD) ~~~~~~~~~~~~#
# Klasse "Highscore", hier ist die Arbeit mit File
class Highscore:
    # Liste mit Daten aus Datei lesen
    def __init__(self):
        self.liste = []
        # Wenn keine Datei da ist, kann noch nichts ausgelesen werden
        if not glob.glob("highscore.csv"):
            return
        d = open("highscore.csv") #Öffnen
        zeile = d.readline() 
        while zeile:
            teil = zeile.split(";")
            name = teil[0]
            score = teil[1][0:len(teil[1])-1]
            score = score.replace(",", ".")
            self.liste.append([name, float(score)])
            zeile = d.readline()
        d.close() #Schließen

    # Liste ändern
    def aendern(self, name, score):
        # Mitten in Liste schreiben
        gefunden = False
        for i in range(len(self.liste)): #Es wird durch jede Zeile iteriert, und der Score an passende Stelle eingesetzt
            # Einsetzen und sortieren in Liste
            if score > self.liste[i][1]:
                self.liste.insert(i, [name, score])
                gefunden = True
                break
        # Letzten Platz ans Ende der Liste schreiben
        if not gefunden:
            self.liste.append([name, score])

    # Geänderte Liste in Datei speichern
    def speichern(self, name, score):
        self.aendern(name, score)
        d = open("highscore.csv", "w") # Wird erstellt falls nicht vorhanden
        for element in self.liste: #Für jede Zeile
            name = element[0]
            score = str(element[1]).replace(".", ",")
            d.write(name + ";" + score + "\n") #Daten und Zeilenumbruch einfügen
        d.close()

    # String ausgeben, der die Highscoreliste beinhaltet
    def __str__(self):
        # Highscore nicht vorhanden (keine Zeilen da)
        if not self.liste:
            return "Keine Highscores vorhanden"
        # Ausgabe Highscore
        ausgabe = "Name            Punkte\n"
        for i in range(len(self.liste)):
            ausgabe += f"{i+1:2d}. {self.liste[i][0]:10}" \
                       f"{self.liste[i][1]:5.2f}\n"
            if i >= 5: #Highscore wird nur bis zum 5.Besten angezeigt
                break
        return ausgabe
#Klasse des Spiels, die alle Daten beinhaltet, ist mit Record gleichzusetzen
class Spiel:
    def __init__(self): #Initialisieren der Eigenschaften, Festlegung Datentyp
        self.spieler = 0
        self.schwierigkeit = 0
        self.highscore = 0
        self.anzahl = 0
        self.richtig = 0
        self.falsch = 0
        self.dauer = 0
        self.zeit_pro_aufgabe = 0
        self.aufgaben = []
        self.loesungen = []
#~~~~~~~~~~~~ KLASSEN (RECORD) ~~~~~~~~~~~~#

#~~~~~~~~~~~~ FUNKTIONEN ~~~~~~~~~~~~#
# Funktion, die bei "Highscore" ausgeführt wird
def highscore_anzeigen():
    global spiel_begonnen
    global highscore_geklickt
    if spiel_begonnen == False:
        highscore_geklickt = True
        tkinter.messagebox.showinfo("Highscore", str(Highscore()))
    #Spiel auffangen
    else:
        tkinter.messagebox.showerror(message="Das Spiel läuft bereits!")
# globale Schwierigkeit wird auf Auswahl gesetzt
def callback_schwierigkeit(selection):
    global schwierigkeit
    global schwierigkeit_gesetzt
    schwierigkeit_gesetzt = True
    schwierigkeit = selection
#Funktion, die beim Start des Spiels ausgeführt wird
def starte_spiel():
    global anzahl
    global gültige_anzahl
    global anzahl_entry
    global spiel_begonnen
    global start_zeit
    global highscore_geklickt
    global schwierigkeit_gesetzt
    global anzahl_entry
    start_zeit = time.time()
    try:
        anzahl=int(anzahl_entry.get())
        if anzahl > 0:
            gültige_anzahl = True
        if anzahl <= 0:
            gültige_anzahl = False
    except:
        gültige_anzahl = False
    # Schwierigkeit und Anzahl sind gewählt
    
    if schwierigkeit_gesetzt == True and gültige_anzahl == True and spiel_begonnen == False:  
        spiel_begonnen = True
        warte_var.set(1)
    elif schwierigkeit_gesetzt == False:
        tkinter.messagebox.showerror(message="Wähle eine Schwierigkeit!")
    elif gültige_anzahl == False:
        tkinter.messagebox.showerror(message="Keine gültigen Aufgabenzahl!")
    elif spiel_begonnen == True:
        tkinter.messagebox.showerror(message="Das Spiel läuft bereits!")
#Funktion, die in Listen gespeicherte Ergebnisse miteinander vergleicht
def pruefen(anzahl, eingabe_liste, ergebnis_liste):
    global richtig
    for i in range(anzahl):
        #korrigieren von falschen Eingaben, Abfangen
        try:
            if int(eingabe_liste[i].get()) == ergebnis_liste[i]:
                korrekt_liste[i].config(text="✓", justify="left")
                richtig = richtig + 1
            else:
                korrekt_liste[i].config(text=ergebnis_liste[i], justify="left")
        except:
            korrekt_liste[i].config(text=ergebnis_liste[i], justify="left")
# Funktion, die bei "fertig" ausgeführt wird
def auswertung():
    global anzahl
    global eingabe_liste
    global ergebnis_liste
    global fertig_gerechnet
    global beschreibung_label
    global schwierigkeit
    global spiel_begonnen
    global high_score
    global name
    if fertig_gerechnet == False:
        name = name_entry.get()
        fertig_gerechnet = True
        warte_var2.set(1)
        pruefen(anzahl, eingabe_liste, ergebnis_liste)
        zeit = zeit_label.cget("text") #Zeit aus Label ziehen
        zeit = zeit.split()
        high_score = score(schwierigkeit, anzahl, richtig, (anzahl-richtig), float(zeit[1]))
        #Eintragung in Highscore
        hs = Highscore()
        hs.speichern(name=name, score=high_score)
        #Feedback wird gegeben
        feedback_label.config(text=f"{richtig} von {anzahl} richtig", justify="left")
        score_label.config(text=f"Punkte: {high_score}", justify="left")
        spiel_begonnen = False
#Funktion, die das Label mit der verbrauchten Zeit verändert
def zeit_anzeigen():
    #Läuft nur, wenn noch nicht fertig
    if fertig_gerechnet == False:
        current_time = time.time() - start_zeit
        zeit_label.config(text=f"Zeit: {round(current_time, 3)} s", justify="left")
        zeit_label.after(100,zeit_anzeigen)
    if fertig_gerechnet == True:
        pass     
# Funktion, die das Programm unverzüglich beendet
def beenden():
    print("Bis zum nächsten Mal!")
    main.destroy()
# Funktion, die die aktuelle Zeit als String zurückgibt
def get_current_time():
  # Get the current time
  now = datetime.now()

  # Format the time as a string
  time_string = now.strftime("%H:%M:%S")

  return time_string
# Funktion, die ein Spiel des Datentyps Spiel() in einer Datei speichert 
def spiel_abspeichern(spiel):
    time.sleep(1)
    with open(f"{spiel.spieler}_{get_current_time()}.txt", "w") as f:
    # Daten in Datei schreiben
        f.write(f"Das Kopfrechenspiel\n")
        f.write(f"\n")
        f.write(f"Spieler: {spiel.spieler}\n")
        f.write(f"Anzahl Aufgaben: {spiel.anzahl}\n")
        f.write(f"Schwierigkeit: {spiel.schwierigkeit}\n")
        f.write(f"Score: {spiel.highscore}\n")
        f.write(f"Dauer: {spiel.dauer}\n")
        f.write(f"Zeit pro Aufgabe: {spiel.zeit_pro_aufgabe}\n")
        for aufgabe in spiel.aufgaben:
            f.write(f"→ {aufgabe}\n")
        f.write(f"{spiel.richtig} von {spiel.anzahl} Aufgaben richtig beantwortet ({spiel.falsch} falsch)")
#Funktion, die die Daten des Spiels in einem Record abspeichert und diesen zurückgibt
def spiel_statistik():
    global aufgaben_liste
    global ergebnis_liste
    global eingabe_liste
    global op_liste
    global korrekt_liste
    global a_liste
    global b_liste
    global anzahl
    global name_entry
    global schwierigkeit
    global zeit_label
    spiel = Spiel()
    spiel.anzahl = anzahl
    for i in range(anzahl):
        aufgabe = f"{a_liste[i]} {op_liste[i]} {b_liste[i]} = {ergebnis_liste[i]} (Eingabe: {eingabe_liste[i].get()})"
        aufgaben_liste.append(aufgabe)
    spiel.aufgaben = aufgaben_liste
    spiel.falsch = anzahl - richtig
    spiel.richtig = richtig
    spiel.spieler = name_entry.get()
    zeit = zeit_label.cget("text")
    zeit = zeit.split()
    spiel.dauer = float(zeit[1])
    spiel.zeit_pro_aufgabe = spiel.dauer / spiel.anzahl
    spiel.schwierigkeit = schwierigkeit
    spiel.highscore = score(spiel.schwierigkeit, anzahl, spiel.richtig, spiel.falsch, spiel.dauer)
    return spiel
# Funktion, die ausgeführt werden, sobald man die Anforderung der Statistiken stellt
def statistiken():
    global stats_runtergeladen
    if stats_runtergeladen == False: #einmaliges runterladen
        spiel = spiel_statistik()
        spiel_abspeichern(spiel)
        stats_runtergeladen = True
# Funktion, die nach benötigten Angaben den aktuellen Score berechnet
def score(schwierigkeit, anzahl, richtige, falsche, zeit):

    try: # x/0 error abfangen
        if schwierigkeit == "LEICHT": 
            score = (richtige / zeit) * 80 - (falsche / anzahl)
        if schwierigkeit == "MITTEL": 
            score = (richtige / zeit) * 100 - (falsche / anzahl)
        if schwierigkeit == "SCHWER": 
            score = (richtige / zeit) * 120 - (falsche / anzahl)
        # kein negativer Highscore (wenn man so schlecht ist)
        if score > 0:
            return round(score, 4)
        else: 
            return 0
    except:
        return 0


def zerstören():
    for widget in main.winfo_children():
        widget.destroy()
#~~~~~~~~~~~~ FUNKTIONEN ~~~~~~~~~~~~#
while True:
    #~~~~~~~~~~~~ GUI ~~~~~~~~~~~~#
    #~~~~~~~~~~~~ SEKTION 1 ~~~~~~~~~~~~#
    #Formatierendes Label bei Titel
    format_label = tkinter.Label(main, text="          ")
    format_label.grid(row=0, column=0)
    #Formatierendes Label bei Name
    format_label3 = tkinter.Label(main, text="          ")
    format_label3.grid(row=1, column=0, pady=(5,5))
    #Formatierendes Label bei Anzahl
    format_label3 = tkinter.Label(main, text="          ")
    format_label3.grid(row=2, column=0, pady=(5,5))
    #Formatierendes Label bei Start
    format_label4 = tkinter.Label(main, text="          ")
    format_label4.grid(row=3, column=0, pady=(5,5))
    #Formatierendes Label bei Aufgabe Nr.1
    format_label4 = tkinter.Label(main, text="          ")
    format_label4.grid(row=4, column=0)
    # Titelfeld
    titel_label = tkinter.Label(main, text="Der Kopfrechnen-Übungsmeister", font=("Helvetica", "20"))
    titel_label.grid(row=0, column=1, columnspan=2, sticky=tkinter.EW, pady=(20,20))
    #Nameentry (EINGABE)
    name_entry = tkinter.Entry(main)
    name_entry.insert(0, "Name eingeben")
    name_entry.grid(row=1, column=1, columnspan=1, sticky=tkinter.EW)
    #Startknopf (BEFEHL)
    start_button = tkinter.Button(main, text="Start", command=lambda: starte_spiel())
    start_button.grid(row=3, column=1, sticky=tkinter.EW)
    #Highscoreknopf (BEFEHL)
    highscore_button = tkinter.Button(main, text="Highscore", command=lambda: highscore_anzeigen())
    highscore_button.grid(row=3, column=2, sticky=tkinter.EW)
    #Schwierigkeit (EINGABE)
    schwierigkeit_variable = tkinter.StringVar(main)
    schwierigkeit_variable.set("Schwierigkeit wählen")
    schwierigkeit_menu = tkinter.OptionMenu(main, schwierigkeit_variable, "LEICHT", "MITTEL", "SCHWER", command=callback_schwierigkeit)
    schwierigkeit_menu.grid(row=1, column=2, columnspan=1,sticky=tkinter.EW)
    #Anzahl Eingabe (EINGABE)
    anzahl_entry = tkinter.Entry(main)
    anzahl_entry.insert(0, 5)
    anzahl_entry.grid(row=2, column=1, columnspan=1, sticky=tkinter.EW)
    #Anzahl Label
    anzahl_label = tkinter.Label(main, text="<--- Anzahl an Aufgaben", justify="left")
    anzahl_label.grid(row=2, column=2, columnspan=1, sticky=tkinter.W)
    #~~~~~~~~~~~~ SEKTION 1 ~~~~~~~~~~~~#

    #Es geht erst weiter, wenn der Start-Button geklickt ist
    start_button.wait_variable(warte_var)

    #~~~~~~~~~~~~ SEKTION 2 ~~~~~~~~~~~~#
    # gesamter Abschnitt, welcher Aufgaben und Eingaben konfiguriert
    def aufgaben_erstellen(anzahl, schwierigkeit):
        # Global, damit andere Funktionen sie verändert nutzen können
        global ergebnis_liste
        global eingabe_liste
        global op_liste
        global korrekt_liste
        global a_liste
        global b_liste
        for i in range(anzahl):
            #Definieren der Aufgaben nach Schwierigkeitsgrad
            #SChwierigkeit 1
            if schwierigkeit == "LEICHT":
                a = random.randint(1,30)
                b = random.randint(1,30)
                op = "+" #Mögliche Operatoren: +
                # Werte werden für spätere Verwendung in Listen gepackt
                op_liste.append(op)
                ergebnis_liste.append(ops[op](a,b))
                a_liste.append(a)
                b_liste.append(b)
            #Schwierigkeit 2
            if schwierigkeit == "MITTEL":
                a = random.randint(1,50)
                b = random.randint(1,50)
                op = random.choice(["+", "-", "*"]) #Mögliche Operatoren: +, -, *
                if op == "-": #Sichergehen, dass nichts negatives rauskommt
                    while a < b:
                        a = random.randint(1,50)
                        b = random.randint(1,50)
                if op == "*": #Sichergehen, dass es nicht zu schwer wird
                    while a > 12 or b > 12:
                        a = random.randint(1,50)
                        b = random.randint(1,50)
                op_liste.append(op)
                ergebnis_liste.append(ops[op](a,b))
                a_liste.append(a)
                b_liste.append(b)
            #Schwierigkeit 3
            if schwierigkeit == "SCHWER":
                a = random.randint(1,100)
                b = random.randint(1,100)
                op = random.choice(["+", "-", "*","/"]) #Mögliche Operatoren: +, -, *, /
                if op == "-": #Sichergehen, dass nichts negatives rauskommt
                    while a < b:
                        a = random.randint(1,100)
                        b = random.randint(1,100)
                if op == "*": #Sichergehen, dass es nicht zu schwer wird
                    while a > 20 or b > 20:
                        a = random.randint(1,100)
                        b = random.randint(1,100)
                if op == "/": #Sichergehen, dass ganzzahliges Ergebnis
                    while a % b != 0:
                        a = random.randint(1,100)
                        b = random.randint(1,100)
                op_liste.append(op)
                ergebnis_liste.append(ops[op](a,b))
                a_liste.append(a)
                b_liste.append(b)
            # Aufgabenstellung
            tkinter.Label(main, text=f"{i + 1}.  {a} {op} {b} =")\
            .grid(row=i+4, column=1, sticky=tkinter.W, padx=(50,0))
            # Eingabefelder
            eingaben = tkinter.Entry(main)
            eingaben.grid(row=i+4, column=2, sticky=tkinter.EW)
            eingabe_liste = eingabe_liste + [eingaben] #Liste mit Verweis auf Feld
            #Spätere Korrekturfelder
            korrekt_Label = tkinter.Label(main, text="", justify="left")
            korrekt_Label.grid(row=i+4, column=3, sticky=tkinter.W)
            korrekt_liste = korrekt_liste + [korrekt_Label]

    aufgaben_erstellen(anzahl, schwierigkeit)
    # "Stoppuhr"
    zeit_label = tkinter.Label(main)
    zeit_label.grid(row=anzahl + 9, column=1, sticky=tkinter.W, padx=(50,0))
    zeit_anzeigen() #"Stoppuhr" unten erscheint
    # Ergebnis (BEFEHL)
    fertig_button = tkinter.Button(main, text="Fertig", command=lambda: auswertung())
    fertig_button.grid(row=anzahl + 9, column=2, columnspan=1, sticky=tkinter.EW)
    # Blueprint Feedback
    feedback_label = tkinter.Label(main, text="", justify="left")
    feedback_label.grid(row=anzahl + 11, column=2, columnspan=1, sticky=tkinter.W, padx=(50,0))
    # Blueprint Score
    score_label = tkinter.Label(main, text="", justify="left")
    score_label.grid(row=anzahl + 11, column=1, columnspan=1, sticky=tkinter.W, padx=(50,0))
    #~~~~~~~~~~~~ SEKTION 2 ~~~~~~~~~~~~#

    #Es geht erst weiter, wenn der Fertig-Button geklickt ist
    fertig_button.wait_variable(warte_var2)

    #~~~~~~~~~~~~ SEKTION 3 ~~~~~~~~~~~~#
    # Beenden (EINGABE
    beenden_button = tkinter.Button(main, text="Spiel schließen", command=lambda: beenden())
    beenden_button.grid(row=anzahl + 12, column=2, columnspan=1, sticky=tkinter.EW)
    # Stats (EINGABE)
    stats_button = tkinter.Button(main, text="Statistiken speichern", command=lambda: statistiken())
    stats_button.grid(row=anzahl + 12, column=1, columnspan=1, sticky=tkinter.EW)
    #~~~~~~~~~~~~ SEKTION 3 ~~~~~~~~~~~~#
    #~~~~~~~~~~~~ GUI ~~~~~~~~~~~~#

# PROGRAMM LÄUFT
main.mainloop()