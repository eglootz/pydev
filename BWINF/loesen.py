import einlesen as e

sudoku1, sudoku2 = e.einlesen("sudoku0.txt")

def loesen(sudoku1, sudoku2):
    liste1 = []
    for key, value in sudoku1.items():
        liste1 = liste1 + [value]

    liste2 = []
    for key, value in sudoku2.items():
        liste2 = liste2 + [value]

    M = 9
    def puzzle(a):
        for i in range(M):
            for j in range(M):
                print(a[i][j],end = " ")
            print()
    def solve(grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
             
        for x in range(9):
            if grid[x][col] == num:
                return False
 
 
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True
 
    def Suduko(grid, row, col):
 
        if (row == M - 1 and col == M):
            return True
        if col == M:
            row += 1
            col = 0
        if grid[row][col] > 0:
            return Suduko(grid, row, col + 1)
        for num in range(1, M + 1, 1): 
     
            if solve(grid, row, col, num):
         
                grid[row][col] = num
                if Suduko(grid, row, col + 1):
                    return True
            grid[row][col] = 0
        return False
 

    grid1 = liste1
    grid2 = liste2
 
    print("~~~~~~~~~~~~~")

    if (Suduko(grid1, 0, 0)):
        puzzle(grid1)
    else:
        print("Lösung 1 existiert nicht :(")

    print("~~~~~~~~~~~~~")


    if (Suduko(grid2, 0, 0)):
        puzzle(grid2)
    else:
        print("Lösung 2 existiert nicht:(")