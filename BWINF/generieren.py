import permutations as p

def generieren(sudoku):
    sudokuliste = []
    zeilenblockpermutationen = [p.zeilenblockABC(sudoku),p.zeilenblockACB(sudoku),p.zeilenblockBAC(sudoku),p.zeilenblockBCA(sudoku),p.zeilenblockCAB(sudoku),p.zeilenblockCBA(sudoku)]
    spaltenblockpermutationen = [p.spaltenblock123(sudoku),p.spaltenblock132(sudoku),p.spaltenblock213(sudoku),p.spaltenblock231(sudoku),p.spaltenblock312(sudoku),p.spaltenblock321(sudoku)]
    zeilenpermutationen = [p.zeileA1A2A3(sudoku),p.zeileA1A3A2(sudoku),p.zeileA2A1A3(sudoku),p.zeileA2A3A1(sudoku),p.zeileA3A1A2(sudoku),p.zeileA3A2A1(sudoku),p.zeileB1B2B3(sudoku),p.zeileB1B3B2(sudoku),p.zeileB2B1B3(sudoku),p.zeileB2B3B1(sudoku),p.zeileB3B1B2(sudoku),p.zeileB3B2B1(sudoku),p.zeileC1C2C3(sudoku),p.zeileC1C3C2(sudoku),p.zeileC2C1C3(sudoku),p.zeileC2C3C1(sudoku),p.zeileC3C1C2(sudoku),p.zeileC3C2C1(sudoku)]
    spaltenpermutationen = [p.spalte1A1B1C(sudoku),p.spalte1A1C1B(sudoku),p.spalte1B1A1C(sudoku),p.spalte1B1C1A(sudoku),p.spalte1C1A1B(sudoku),p.spalte1C1B1A(sudoku),p.spalte2A2B2C(sudoku),p.spalte2A2C2B(sudoku),p.spalte2B2A2C(sudoku),p.spalte2B2C2A(sudoku),p.spalte2C2A2B(sudoku),p.spalte2C2B2A(sudoku),p.spalte3A3B3C(sudoku),p.spalte3A3C3B(sudoku),p.spalte3B3A3C(sudoku),p.spalte3B3C3A(sudoku),p.spalte3C3A3B(sudoku),p.spalte3C3B3A(sudoku)]
    for permutation1 in zeilenblockpermutationen:
        for permutation2 in spaltenblockpermutationen:
             for permutation3 in zeilenpermutationen:
                 for permutation4 in spaltenpermutationen:  
                    sudoku = permutation1
                    sudokuliste = sudokuliste + [sudoku]
                    sudoku = permutation2
                    sudokuliste = sudokuliste + [sudoku]
                    sudoku = permutation3
                    sudokuliste = sudokuliste + [sudoku]
                    sudoku = permutation4
                    sudokuliste = sudokuliste + [sudoku]
    return sudokuliste


"""
M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()

for item in sudokuliste:
    print("~~~~~~~~~~~~~~~~")
    puzzle(item)

"""