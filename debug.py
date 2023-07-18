import grid_handling as gh
from time import sleep as slp
import os

os.system("cls")

gh.populate_grid_with_cells()
gh.get_visual_data_for_cells()

for t in range(301):
    os.system("cls")
    gh.neighbor_check()
    gh.update_grid()
    slp(1.0)
