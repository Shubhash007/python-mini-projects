board =[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
txt1 = "800000000003600000070090200050007000000045700000100030001000068008500010090000400"
def str_to_board(txt):
    txt = txt.replace("-",'0')
    assert len(txt) == 81
    lst = [int(c) for c in txt]
    lst2 = []
    for c in range(0,len(lst)+1,9):
        if c % 9 == 0 and c!=0:
            lst2.append(lst[c-9:c])
    return lst2



def grid(bo):
    for lst in range(len(bo)):
        if lst % 3 == 0 and lst != 0:
            print("------------------------")
        for num in range(len(bo[0])):
            if num % 3 == 0 and num!=0:
                print(" | ", end = "")
            if num == 8:
                print(bo[lst][num])
            else:
                print(str(bo[lst][num])+" ",end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return False


def validity(bo,num,pos):
    # Check if row has same number
    for x in range(9):
        if bo[pos[0]][x] == num and pos[1] != x:
            return False

    #Check if column has same number:
    for y in range(9):
        if bo[y][pos[1]] == num and pos[0] != y:
            return False

    #Check if box has same number:
    row_box = pos[0]//3
    cols_box = pos[1]//3

    for i in range(row_box*3,row_box*3 + 3):
        for j in range(cols_box*3,cols_box*3 + 3):
            if bo[i][j] == num and (i,j) != pos :
                return False
    return True

def solve(bo):
    empty = find_empty(bo)
    if not empty:
        return True
    else:
        row,col = empty

    for i in range(1,10):
        if validity(bo,i,(row,col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False

board1 = str_to_board(txt1)
grid(board)
print("----------------------------------")
solve(board)
grid(board)

'''
7 8 5  | 4 3 9  | 1 2 6
6 1 2  | 8 7 5  | 3 4 9
4 9 3  | 6 2 1  | 5 7 8
- - - - - - - - - - - - -
8 5 7  | 9 4 3  | 2 6 1
2 6 1  | 7 5 8  | 9 3 4
9 3 4  | 1 6 2  | 7 8 5
- - - - - - - - - - - - -
5 7 8  | 3 9 4  | 6 1 2
1 2 6  | 5 8 7  | 4 9 3
3 4 9  | 2 1 6  | 8 5 7
'''
