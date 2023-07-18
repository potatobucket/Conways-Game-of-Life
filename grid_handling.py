import numpy as np
from time import sleep as slp
import os
import cell

#-- determines the size of the grid
rows = int(input("How many rows?\n"))
columns = int(input("How many columns?\n"))

#-- determines how many generations pass in the simulation
generations = int(input("How many generations would you like to simulate?\n"))

#-- creates two grids: one for keeping track of a cell's data and one to track its visual status
cellGrid = np.full(shape = (rows,columns), fill_value = "")
cellGrid = cellGrid.tolist()

visualArray = np.full(shape = (rows, columns), fill_value = "")
visualArray = visualArray.tolist()

#-- changes all the empty elements to cells
def populate_grid_with_cells():
    for i in range(rows):
        for j in range(columns):
            cellGrid[i][j] = cell.Cell()

#-- populates the visual grid with symbols representing a dead cell (▢) and an alive cell (▣)
def get_visual_data_for_cells():
    for a in range(rows):
        for b in range(columns):
            visualArray[a][b] = cellGrid[a][b].visual
    for c in range(rows):
        print(visualArray[c])

#-- checks each cell for living neighbors (only checks the inner cells but each cell does exclude itself)
def neighbor_check():
    for w in range(1, rows - 1):
        for v in range(1, columns - 1):
            cellGrid[w][v].neighbors = 0
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if cellGrid[w + z][v + y].alive == True and cellGrid[w + z][v + y] != cellGrid[w][v]:
                        cellGrid[w][v].neighbors += 1

#-- updates each cell in the grid('s center) relative to how many neighbors it has, updates the visual grid
#-- and reprints it to the terminal
def update_grid():
    for gridRow in range(1, rows - 1):
        for gridColumn in range(1, columns - 1):
            if cellGrid[gridRow][gridColumn].alive == True and cellGrid[gridRow][gridColumn].neighbors == 2 or cellGrid[gridRow][gridColumn].alive == True and cellGrid[gridRow][gridColumn].neighbors == 3:
                cellGrid[gridRow][gridColumn].alive = True
                cellGrid[gridRow][gridColumn].visual = "▣"
            if cellGrid[gridRow][gridColumn].alive == True and cellGrid[gridRow][gridColumn].neighbors < 2 or cellGrid[gridRow][gridColumn].alive == True and cellGrid[gridRow][gridColumn].neighbors > 3:
                cellGrid[gridRow][gridColumn].alive = False
                cellGrid[gridRow][gridColumn].visual = "▢"
            if cellGrid[gridRow][gridColumn].alive == False and cellGrid[gridRow][gridColumn].neighbors == 3:
                cellGrid[gridRow][gridColumn].alive = True
                cellGrid[gridRow][gridColumn].visual = "▣"
    get_visual_data_for_cells()

#-- runs the game for the specified number of generations
def run_game_for_(generations):
    for t in range(generations + 1):
        os.system("cls")
        neighbor_check()
        update_grid()
        slp(0.034)
