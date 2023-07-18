import grid_handling as gh

gh.populate_grid_with_cells()
gh.get_visual_data_for_cells()

# detectArea = [
#     [(-1, -1), (-1, 0), (-1, 1)],
#     [(0, -1), (0, 0), (0, 1)],
#     [(1, -1), (1, 0), (1, 1)]
# ]

def neighborCheck():
    for w in range(1, gh.rows - 1):
        for v in range(1, gh.columns - 1):
            for y in range(-1, 2):
                for z in range(-1, 2):
                    if gh.cellGrid[w + z][v + y].alive == True and gh.cellGrid[w + z][v + y] != gh.cellGrid[w][v]:
                        gh.cellGrid[w][v].neighbors += 1
    for rowcheck in range(1, gh.rows - 1):
        for colcheck in range(1, gh.columns - 1):
            print(f"Number of neighbors for {rowcheck, colcheck}: {gh.cellGrid[rowcheck][colcheck].neighbors}")
