def change01(liste01):

    for sudoku in liste01:
        for zeile in sudoku:
            for item in zeile:
                if item != 0:
                    liste01[sudoku][zeile][item] = 1

    return liste01