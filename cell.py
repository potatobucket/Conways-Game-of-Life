#-- this will be a class for cells
#-- I need to think of what data it needs to keep track of
#-- 
#-- Life status (alive/dead)
#-- Position on grid (x, y) (Maybe posX and posY?)
#-- Number of neighbors

class Cell:
    def __init__(self, alive, posX, posY, neighbors):
        self.alive = alive
        self.posX = posX
        self.posY = posY
        self.neighbors = neighbors
