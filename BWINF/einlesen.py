# ausgabe von Sudokus in Dict Form
def einlesen(filename):
    # initialisieren der Sudoku-Variablen
    sudoku1 = {}
    sudoku2 = {}
    # initialisieren der Nummer, die im dict key erscheint
    x = 1
    # initialisieren der Zeilennummern
    line_number = 0
    
    with open(f'{filename}', mode='r', encoding='utf-8-sig') as file:
        for line in file:
            line_number = line_number + 1
            row = line.split()
        
            #jedes Element der Zeile wird in int umgewandelt, in eine Liste gepackt, und zwischengespeichert
            row = [int(number) for number in row]
            
            if line_number < 10:
                #schlüssel mit richtiger Bezeichnung wird zugewiesen, Zeile wird Schlüssel zugeordnet
                sudoku1["line{0}".format(x)] = row
                x = x + 1

            # x für Schlüsselnamen wird zurückgesetzt
            if line_number == 10:
                x = 1
            if line_number > 10:
                sudoku2["line{0}".format(x)] = row
                x = x + 1

    # sudokus werden als Dicts zurückgegeben            
    return sudoku1, sudoku2

#initialisieren des datentyps "Sudoku"
class SUDOKU():
    def __init__(self):
        self.line1 = []
        self.line2 = []
        self.line3 = []
        self.line4 = []
        self.line5 = []
        self.line6 = []
        self.line7 = []
        self.line8 = []
        self.line9 = []
        self.column1 = []
        self.column2 = []
        self.column3 = []
        self.column4 = []
        self.column5 = []
        self.column6 = []
        self.column7 = []
        self.column8 = []
        self.column9 = []
        self.sblock1 = []
        self.sblock2 = []
        self.sblock3 = []
        self.zblock1 = []
        self.zblock2 = []
        self.zblock3 = []


# Funktion, welche nach Angabe der Spalte durch das dict geht, und jeweils den Wert aus der Liste der Zeile zieht
def get_column(spalte, d):
    column = []
    #for i in range(9):

    # wir getten jetzt die zeile und filtern daraus das jeweilige element
    for i in range(1,10):
        column = column + [d.get(f"line{i}")[spalte]]
    
    #print(column)
    return column


# zuweisung der dict-sudokus zum datentyp
def zuweisung(d):
    sudoku = SUDOKU()
    # zeilen werden direct aus dem dict übernommen
    sudoku.line1 = d["line1"]
    sudoku.line2 = d["line2"]
    sudoku.line3 = d["line3"]
    sudoku.line4 = d["line4"]
    sudoku.line5 = d["line5"]
    sudoku.line6 = d["line6"]
    sudoku.line7 = d["line7"]
    sudoku.line8 = d["line8"]
    sudoku.line9 = d["line9"]
    # spalten werden rausgefiltert
    sudoku.column1 = get_column(0,d)
    sudoku.column2 = get_column(1,d)
    sudoku.column3 = get_column(2,d)
    sudoku.column4 = get_column(3,d)
    sudoku.column5 = get_column(4,d)
    sudoku.column6 = get_column(5,d)
    sudoku.column7 = get_column(6,d)
    sudoku.column8 = get_column(7,d)
    sudoku.column9 = get_column(8,d)
    # blöcke werden einfach addiert
    sudoku.sblock1 = sudoku.line1 + sudoku.line2 + sudoku.line3
    sudoku.sblock2 = sudoku.line4 + sudoku.line5 + sudoku.line6
    sudoku.sblock3 = sudoku.line7 + sudoku.line8 + sudoku.line9
    sudoku.zblock1 = sudoku.column1 + sudoku.column2 + sudoku.column3
    sudoku.zblock2 = sudoku.column4 + sudoku.column5 + sudoku.column6
    sudoku.zblock3 = sudoku.column7 + sudoku.column8 + sudoku.column9

    # fertiges Datenpaket wird zurückgegeben
    return sudoku