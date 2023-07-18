import random as rndm
import numpy as np

#-- creates a cell object that is randomly alive or dead
class Cell:
    def __init__(self):
        self.alive = rndm.choice([True, False, False, False])
        self.neighbors = 0
        if self.alive == False:
            self.visual = "▢"
        else:
            self.visual = "▣"
        self.coordinateX = 0
        self.coodirnateY = 0
    def life_status(self):
        if self.alive == False:
            return "The cell is dead."
        else:
            return "The cell is alive."

if __name__ == "__main__":
    #-- if you try to fill the array with cells at the outset it fills it with identical cells
    #-- so you have to create an empty array and then change all the elements to cells later
    testArray = np.full(shape = (5, 5), fill_value = "")
    testArray = testArray.tolist()

    #-- gets the size of the created array in both dimensions
    rows = len(testArray)
    columns = len(testArray[0])

    #-- changes all the empty elements to cells
    for i in range(rows):
        for j in range(columns):
            testArray[i][j] = Cell()

    #-- converts the life status of the elements of the cell array to something more visually-friendly
    visualArray = np.full(shape = (rows, columns), fill_value = "")
    visualArray = visualArray.tolist()
    for a in range(rows):
        for b in range(columns):
            visualArray[a][b] = testArray[a][b].visual

    #-- this is just for debugging purposes
    for c in range(rows):
        print(visualArray[c])
