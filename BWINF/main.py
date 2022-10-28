import einlesen as e

sudoku1, sudoku2 = e.einlesen("sudoku0.txt")


print("~~~ Sudoku 1: ~~~")
print(sudoku1)
print("~~~ Sudoku 2: ~~~")
print(sudoku2)


sudoku_class1 = zuweisung(d = sudoku1)
sudoku_class2 = zuweisung(d = sudoku2)


print(sudoku_class1.column1)

print(sudoku_class2)