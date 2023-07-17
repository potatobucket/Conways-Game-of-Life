import numpy as np
import cell

#-- determines the size of the grid
rows = int(input("How many rows?\n"))
columns = int(input("How many columns?\n"))

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

# def grid_handling():
    # for i in range(rows):
    #     for j in range(columns):
    #         if i == verticle and j == horizontal:
    #             cellGridCopy[i][j] = "1"
    #         if i == verticle + 1 and j == horizontal + 1 or i == verticle - 1 and j == horizontal - 1:
    #             cellGridCopy[i][j] = "*"
    #         if i == verticle - 1 and j == horizontal + 1 or i == verticle + 1 and j == horizontal - 1:
    #             cellGridCopy[i][j] = "*"
    #         if i == verticle and j == horizontal + 1 or i == verticle + 1 and j == horizontal:
    #             cellGridCopy[i][j] = "*"
    #         if i == verticle - 1 and j == horizontal or i == verticle and j == horizontal - 1:
    #             cellGridCopy[i][j] = "*"
#     for square in cellGridCopy:
#         print(square)
