import numpy as np

grid = [
    ["0", "0", "0", "0"],
    ["0", "0", "0", "0"],
    ["0", "0", "0", "0"],
    ["0", "0", "0", "0"]
]

testArray = np.full(shape = (4,4), fill_value = "butts")
print(testArray)

horizontal = int(input("X coordinate?\n"))
verticle = int(input("Y coordinate?\n"))

def grid_handling():
    for i in range(4):
        for j in range(4):
            if i == verticle and j == horizontal:
                grid[i][j] = "1"
            if i == verticle + 1 and j == horizontal + 1 or i == verticle - 1 and j == horizontal - 1:
                grid[i][j] = "*"
            if i == verticle - 1 and j == horizontal + 1 or i == verticle + 1 and j == horizontal - 1:
                grid[i][j] = "*"
            if i == verticle and j == horizontal + 1 or i == verticle + 1 and j == horizontal:
                grid[i][j] = "*"
            if i == verticle - 1 and j == horizontal or i == verticle and j == horizontal - 1:
                grid[i][j] = "*"
    for square in grid:
        print(square)
