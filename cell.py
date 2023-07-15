#-- this will be a class for cells
#-- I need to think of what data it needs to keep track of
#-- 
#-- Life status (alive/dead)
#-- Position on grid (x, y) (Maybe posX and posY?)
#-- Number of neighbors

import random as rndm
import numpy as np

class Cell:
    def __init__(self, alive):
        self.alive = alive
    def life_status(self):
        if self.alive == False:
            return "The cell is dead."
        else:
            return "The cell is alive."

testArray = np.full(shape = (2, 4), fill_value = "")
testArray = testArray.tolist()
# testArray = np.copy(testArray)

states = [True, False]

# for i in range(9):
#     print(rndm.choice(states))

rows = len(testArray)
columns = len(testArray[0])

for i in range(rows):
    for j in range(columns):
        testArray[i][j] = Cell(rndm.choice([True, False]))

# for i in range(rows):
#     for j in range(columns):
#         testArray[i][j].alive = rndm.choice(states)

for a in range(rows):
    for b in range(columns):
        print(testArray[a][b].alive)
