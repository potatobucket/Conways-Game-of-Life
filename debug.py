import grid_handling as gh

gh.populate_grid_with_cells()
gh.get_visual_data_for_cells()
gh.neighborCheck()

def update_grid():
    for gridRow in range(1, gh.rows - 1):
        for gridColumn in range(1, gh.columns - 1):
            if gh.cellGrid[gridRow][gridColumn].alive == True and gh.cellGrid[gridRow][gridColumn].neighbors == 2 or gh.cellGrid[gridRow][gridColumn].alive == True and gh.cellGrid[gridRow][gridColumn].neighbors == 3:
                gh.cellGrid[gridRow][gridColumn].alive = True
                gh.cellGrid[gridRow][gridColumn].visual = "▣"
            if gh.cellGrid[gridRow][gridColumn].alive == True and gh.cellGrid[gridRow][gridColumn].neighbors <= 1 or gh.cellGrid[gridRow][gridColumn].alive == True and gh.cellGrid[gridRow][gridColumn].neighbors >= 4:
                gh.cellGrid[gridRow][gridColumn].alive = False
                gh.cellGrid[gridRow][gridColumn].visual = "▢"
            if gh.cellGrid[gridRow][gridColumn].alive == False and gh.cellGrid[gridRow][gridColumn].neighbors == 3:
                gh.cellGrid[gridRow][gridColumn].alive = True
                gh.cellGrid[gridRow][gridColumn].visual = "▣"
    gh.get_visual_data_for_cells()
