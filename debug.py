import grid_handling as gh

gh.populate_grid_with_cells()
gh.get_visual_data_for_cells()

# detectArea = [
#     [(-1, -1), (-1, 0), (-1, 1)],
#     [(0, -1), (0, 0), (0, 1)],
#     [(1, -1), (1, 0), (1, 1)]
# ]

for y in range(-1, 2):
    for z in range(-1, 2):
        if gh.cellGrid[1 - z][1 - y].alive == True:
            gh.cellGrid[1][1].neighbors += 1

print(f"Number of neighbors: {gh.cellGrid[1][1].neighbors}")
