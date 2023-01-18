#PERMUTATIONEN

# zeilenblöcke tauschen
def zeilenblockABC(sudoku):
    sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8] = sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8]
    return sudoku
def zeilenblockACB(sudoku):
    sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8] = sudoku[0],sudoku[1],sudoku[2],sudoku[6],sudoku[7],sudoku[8],sudoku[3],sudoku[4],sudoku[5]
    return sudoku
def zeilenblockBCA(sudoku):
    sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8] = sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8],sudoku[0],sudoku[1],sudoku[2]
    return sudoku
def zeilenblockBAC(sudoku):
    sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8] = sudoku[3],sudoku[4],sudoku[5],sudoku[0],sudoku[1],sudoku[2],sudoku[6],sudoku[7],sudoku[8]
    return sudoku
def zeilenblockCAB(sudoku):
    sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8] = sudoku[6],sudoku[7],sudoku[8],sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5]
    return sudoku
def zeilenblockCBA(sudoku):
    sudoku[0],sudoku[1],sudoku[2],sudoku[3],sudoku[4],sudoku[5],sudoku[6],sudoku[7],sudoku[8] = sudoku[6],sudoku[7],sudoku[8],sudoku[3],sudoku[4],sudoku[5],sudoku[0],sudoku[1],sudoku[2]
    return sudoku

#spaltenblöcke tauschen
def spaltenblock123(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8]
    return sudoku
def spaltenblock132(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5]
    return sudoku
def spaltenblock213(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8]    
    return sudoku
def spaltenblock231(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2]
    return sudoku
def spaltenblock312(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5]
    return sudoku
def spaltenblock321(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2]
    return sudoku

#Zeilen innerhalb der Blöcke tauschen
def zeileA1A2A3(sudoku):
    sudoku[0],sudoku[1],sudoku[2] = sudoku[0],sudoku[1],sudoku[2]
    return sudoku
def zeileA1A3A2(sudoku):
    sudoku[0],sudoku[1],sudoku[2] = sudoku[0],sudoku[2],sudoku[1]
    return sudoku
def zeileA2A1A3(sudoku):
    sudoku[0],sudoku[1],sudoku[2] = sudoku[1],sudoku[0],sudoku[3]
    return sudoku
def zeileA2A3A1(sudoku):
    sudoku[0],sudoku[1],sudoku[2] = sudoku[1],sudoku[2],sudoku[0]
    return sudoku
def zeileA3A1A2(sudoku):
    sudoku[0],sudoku[1],sudoku[2] = sudoku[2],sudoku[0],sudoku[1]
    return sudoku
def zeileA3A2A1(sudoku):
    sudoku[0],sudoku[1],sudoku[2] = sudoku[2],sudoku[1],sudoku[0]
    return sudoku
def zeileB1B2B3(sudoku):
    sudoku[3],sudoku[4],sudoku[5] = sudoku[3],sudoku[4],sudoku[5]
    return sudoku
def zeileB1B3B2(sudoku):
    sudoku[3],sudoku[4],sudoku[5] = sudoku[3],sudoku[5],sudoku[4]
    return sudoku
def zeileB2B1B3(sudoku):
    sudoku[3],sudoku[4],sudoku[5] = sudoku[4],sudoku[3],sudoku[5]
    return sudoku
def zeileB2B3B1(sudoku):
    sudoku[3],sudoku[4],sudoku[5] = sudoku[4],sudoku[5],sudoku[3]
    return sudoku
def zeileB3B1B2(sudoku):
    sudoku[3],sudoku[4],sudoku[5] = sudoku[5],sudoku[3],sudoku[4]
    return sudoku
def zeileB3B2B1(sudoku):
    sudoku[3],sudoku[4],sudoku[5] = sudoku[5],sudoku[4],sudoku[3]
    return sudoku
def zeileC1C2C3(sudoku):
    sudoku[6],sudoku[7],sudoku[8] = sudoku[6],sudoku[7],sudoku[8]
    return sudoku
def zeileC1C3C2(sudoku):
    sudoku[6],sudoku[7],sudoku[8] = sudoku[6],sudoku[8],sudoku[7]
    return sudoku
def zeileC2C1C3(sudoku):
    sudoku[6],sudoku[7],sudoku[8] = sudoku[7],sudoku[6],sudoku[8]
    return sudoku
def zeileC2C3C1(sudoku):
    sudoku[6],sudoku[7],sudoku[8] = sudoku[7],sudoku[8],sudoku[6]
    return sudoku
def zeileC3C1C2(sudoku):
    sudoku[6],sudoku[7],sudoku[8] = sudoku[8],sudoku[6],sudoku[7]
    return sudoku
def zeileC3C2C1(sudoku):
    sudoku[6],sudoku[7],sudoku[8] = sudoku[8],sudoku[7],sudoku[6]
    return sudoku

#Spalten innerhalb der Blöcke tauschen
def spalte1A1B1C(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2] = sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2]
    return sudoku
def spalte1A1C1B(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2] = sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1]
    return sudoku
def spalte1B1A1C(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2] = sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2]
    return sudoku
def spalte1B1C1A(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2] = sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0]
    return sudoku
def spalte1C1A1B(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2] = sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1]
    return sudoku
def spalte1C1B1A(sudoku):
    sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2] = sudoku[0][2],sudoku[1][2],sudoku[2][2],sudoku[3][2],sudoku[4][2],sudoku[5][2],sudoku[6][2],sudoku[7][2],sudoku[8][2],sudoku[0][1],sudoku[1][1],sudoku[2][1],sudoku[3][1],sudoku[4][1],sudoku[5][1],sudoku[6][1],sudoku[7][1],sudoku[8][1],sudoku[0][0],sudoku[1][0],sudoku[2][0],sudoku[3][0],sudoku[4][0],sudoku[5][0],sudoku[6][0],sudoku[7][0],sudoku[8][0]
    return sudoku

def spalte2A2B2C(sudoku):
    sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] = sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] 
    return sudoku
def spalte2A2C2B(sudoku):
    sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] = sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4]
    return sudoku
def spalte2B2A2C(sudoku):
    sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] = sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5]
    return sudoku
def spalte2B2C2A(sudoku):
    sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] = sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3]
    return sudoku
def spalte2C2A2B(sudoku):
    sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] = sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4]
    return sudoku
def spalte2C2B2A(sudoku):
    sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5] = sudoku[0][5],sudoku[1][5],sudoku[2][5],sudoku[3][5],sudoku[4][5],sudoku[5][5],sudoku[6][5],sudoku[7][5],sudoku[8][5],sudoku[0][4],sudoku[1][4],sudoku[2][4],sudoku[3][4],sudoku[4][4],sudoku[5][4],sudoku[6][4],sudoku[7][4],sudoku[8][4],sudoku[0][3],sudoku[1][3],sudoku[2][3],sudoku[3][3],sudoku[4][3],sudoku[5][3],sudoku[6][3],sudoku[7][3],sudoku[8][3]
    return sudoku

def spalte3A3B3C(sudoku):
    sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8]   
    return sudoku
def spalte3A3C3B(sudoku):
    sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7]
    return sudoku
def spalte3B3A3C(sudoku):
    sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8]
    return sudoku
def spalte3B3C3A(sudoku):
    sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6]
    return sudoku
def spalte3C3A3B(sudoku):
    sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7]
    return sudoku
def spalte3C3B3A(sudoku):
    sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8] = sudoku[0][8],sudoku[1][8],sudoku[2][8],sudoku[3][8],sudoku[4][8],sudoku[5][8],sudoku[6][8],sudoku[7][8],sudoku[8][8],sudoku[0][7],sudoku[1][7],sudoku[2][7],sudoku[3][7],sudoku[4][7],sudoku[5][7],sudoku[6][7],sudoku[7][7],sudoku[8][7],sudoku[0][6],sudoku[1][6],sudoku[2][6],sudoku[3][6],sudoku[4][6],sudoku[5][6],sudoku[6][6],sudoku[7][6],sudoku[8][6]
    return sudoku

    