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


#-- if you try to fill the array with cells at the outset it fills it with identical cells
#-- so you have to create an empty array and then change all the elements to cells later
testArray = np.full(shape = (2, 4), fill_value = "")
testArray = testArray.tolist()

#-- gets the size of the created array in both dimensions
rows = len(testArray)
columns = len(testArray[0])

#-- changes all the empty elements to cells
for i in range(rows):
    for j in range(columns):
        testArray[i][j] = Cell()

#-- this is just for debugging purposes
for a in range(rows):
    for b in range(columns):
        print(testArray[a][b].alive)
