import grid_handling as gh
from time import sleep as slp
import os

os.system("cls")

gh.populate_grid_with_cells()
gh.get_visual_data_for_cells()

def run_game_for_(generations):
    for t in range(generations):
        os.system("cls")
        gh.neighbor_check()
        gh.update_grid()
        slp(0.034)
