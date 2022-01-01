# Conway's Game of Life
import random, time, copy, sys
WIDTH = 20
HEIGHT = 10

nextCells = []
for x in range(WIDTH):
    soul = {0:"#",1:"-"}
    column = []
    for y in range(HEIGHT):
        column.append(soul[random.randint(0,1)])
    nextCells.append(column)
    print("".join(column))

while True:
    print('\n\n\n')
    print("Current cells")
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y],end="")
        print()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            leftie  = (x-1)  % WIDTH
            rightie = (x+1)  % WIDTH
            up      = (y+1)  % HEIGHT
            down    = (y-1)  % HEIGHT

            aliveppl = 0
            if currentCells[leftie][up] == "#":
                aliveppl += 1
            if currentCells[x][up] == "#":
                aliveppl += 1
            if currentCells[rightie][up] == "#" :
                aliveppl += 1
            if currentCells[leftie][y] == "#":
                aliveppl += 1
            if currentCells[rightie][y] == "#"  :
                aliveppl += 1
            if currentCells[leftie][down] == "#":
                aliveppl += 1
            if currentCells[x][down] == "#":
                aliveppl += 1
            if currentCells[rightie][down] == "#":
                aliveppl += 1


            if currentCells[x][y] == "#" and (aliveppl==3 or aliveppl == 2):
                nextCells[x][y] = "#"
            elif currentCells[x][y] == "-" and aliveppl == 3:
                nextCells[x][y] = "#"
            else:
                nextCells[x][y] = "-"
    time.sleep(0.5)
    sys.exit()
