import numpy as np

rows = int(input("How many rows?\n"))
columns = int(input("How many columns?\n"))

grid = np.full(shape = (rows,columns), fill_value = "0")
newGrid = np.copy(grid)

horizontal = int(input("X coordinate?\n"))
verticle = int(input("Y coordinate?\n"))

def grid_handling():
    for i in range(rows):
        for j in range(columns):
            if i == verticle and j == horizontal:
                newGrid[i][j] = "1"
            if i == verticle + 1 and j == horizontal + 1 or i == verticle - 1 and j == horizontal - 1:
                newGrid[i][j] = "*"
            if i == verticle - 1 and j == horizontal + 1 or i == verticle + 1 and j == horizontal - 1:
                newGrid[i][j] = "*"
            if i == verticle and j == horizontal + 1 or i == verticle + 1 and j == horizontal:
                newGrid[i][j] = "*"
            if i == verticle - 1 and j == horizontal or i == verticle and j == horizontal - 1:
                newGrid[i][j] = "*"
    for square in newGrid:
        print(square)
