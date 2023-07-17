import numpy as np
import cell

testArray = np.full(shape = (3, 3), fill_value = "x, y")
testArray = testArray.tolist()

rows = len(testArray)
columns = len(testArray[0])

aliveArray = np.full(shape = (rows, columns), fill_value = "")
aliveArray = aliveArray.tolist()

coordinateArray = np.full(shape = (rows, columns), fill_value = "")
coordinateArray = coordinateArray.tolist()

for a in range(rows):
    for b in range(columns):
        testArray[a][b] = cell.Cell()

visualArray = np.full(shape = (rows, columns), fill_value = "")
visualArray = visualArray.tolist()
for g in range(rows):
    for h in range(columns):
        visualArray[g][h] = testArray[g][h].visual

for e in range(rows):
    for f in range(columns):
        aliveArray[e][f] = testArray[e][f].alive

for c in range(rows):
    for d in range(columns):
        testArray[c][d].coordinateX = d
        testArray[c][d].coordinateY = c

for k in range(rows):
    for l in range(columns):
        coordinateArray[k][l] = f"({testArray[k][l].coordinateX}, {testArray[k][l].coordinateY})"

for y in range(rows):
    print(visualArray[y], coordinateArray[y])

testX = int(input("Which X ya like to test, guvnah?\n"))
testY = int(input("Which Y ya like to test, guvnah?\n"))

def countNeighbors(grid, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if testArray[x + i][y + j].alive == True:
                sum +=1
    sum -= 1
    return sum

print(countNeighbors(testArray, testX, testY))

# print("Number of neighbors: ", testArray[testX][testY].neighbors)

# for poop in range(rows):
#     print(aliveArray[poop])


# for doodle in range(rows):
#     for daddle in range(columns):
#         print(testArray[doodle][daddle].coordinateX, testArray[doodle][daddle].coordinateY, testArray[doodle][daddle].alive)

# for deedle in range(rows):
#     print(visualArray[deedle], coordinateArray[deedle])
