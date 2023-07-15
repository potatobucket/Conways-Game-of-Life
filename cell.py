import random as rndm
import numpy as np

#-- creates a cell object that is randomly alive or dead
class Cell:
    def __init__(self):
        self.alive = rndm.choice([True, False])
    def life_status(self):
        if self.alive == False:
            return "The cell is dead."
        else:
            return "The cell is alive."

testArray = np.full(shape = (2, 4), fill_value = "")
testArray = testArray.tolist()

rows = len(testArray)
columns = len(testArray[0])

for i in range(rows):
    for j in range(columns):
        testArray[i][j] = Cell()

for a in range(rows):
    for b in range(columns):
        print(testArray[a][b].alive)
