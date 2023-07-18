import grid_handling as gh

gh.populate_grid_with_cells()
gh.get_visual_data_for_cells()
gh.neighborCheck()

newCellGrid = gh.np.full(shape = (gh.rows, gh.columns), fill_value = "")
newCellGrid = newCellGrid.tolist()

for hook in range(1, gh.rows - 1):
    for smee in range(1, gh.rows - 1):
        if gh.cellGrid[hook][smee].alive == True and gh.cellGrid[hook][smee].neighbors == 2 or gh.cellGrid[hook][smee].alive == True and gh.cellGrid[hook][smee].neighbors == 3:
            gh.cellGrid[hook][smee].alive = True
            gh.cellGrid[hook][smee].visual = "▣"
        if gh.cellGrid[hook][smee].alive == True and gh.cellGrid[hook][smee].neighbors <= 1 or gh.cellGrid[hook][smee].alive == True and gh.cellGrid[hook][smee].neighbors >= 4:
            gh.cellGrid[hook][smee].alive = False
            gh.cellGrid[hook][smee].visual = "▢"
        if gh.cellGrid[hook][smee].alive == False and gh.cellGrid[hook][smee].neighbors == 3:
            gh.cellGrid[hook][smee].alive = True
            gh.cellGrid[hook][smee].visual = "▣"

gh.get_visual_data_for_cells()
