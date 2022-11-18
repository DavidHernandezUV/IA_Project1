import numpy as np


class Node:
    # CONSTANTS
    LEFT = 0
    DOWN = 1
    RIGHT = 2
    UP = 3
    EMPTY = 0
    BLOCK = 1
    MARIO = 2
    STAR = 3
    FLOWER = 4
    KOOPA = 5
    YOSHI = 6

    # Costs
    KOOPA_COST = 5
    MOVE_COST = 1
    MOVE_WITH_STAR_COST = 0.5

    # Powerups
    STAR_POWER = 6
    BULLETS = 1

    def __init__(self, gameBoard, father, operator, depth, marioPos, yoshiPos):
        self.gameBoard = gameBoard
        self.father = father
        self.operator = operator
        self.depth = depth
        self.ROWS = len(gameBoard)
        self.COLS = len(gameBoard[0])
        self.marioPos = marioPos
        self.yoshiPos = yoshiPos

        if depth == 0:
            self.cost = 0
            self.flowers_acum = 0
            self.star_effect = 0
        else:

            self.star_effect = father.getStar_effect()
            self.flowers_acum = father.getFlower_acum()
            # Game character that was in the position that Mario occupies now
            self.gameCharacter = self.father.getGameBoard()[self.marioPos]
            self.cost = father.getCost() + self.checkCost()
            # should spend before taking any a powerup
            #print("bef", self.marioPos, self.cost)
            self.checkPowerUps()
            self.spendPowerUps()
            #print("aft", self.marioPos, self.cost)

    def getMarioPos(self):
        return self.marioPos

    def getGameBoard(self):
        return self.gameBoard

    def getCost(self):
        return self.cost

    def getDepth(self):
        return self.depth

    def getFather(self):
        return self.father

    def getStar_effect(self):
        return self.star_effect

    def getFlower_acum(self):
        return self.flowers_acum
    # move: number -> matrix, tuple
    # Checks if it is possible to move in a given direction (not going through block or limit)

    def move(self, direction):

        # create copied son
        sonGameBoard = np.array(self.gameBoard, copy=True)
        sonMarioPosition = self.marioPos

        # Checks if there is no limit or block
        # MOVE TO LEFT
        if direction == self.LEFT and (self.marioPos[1]-1 >= 0) and (sonGameBoard[self.marioPos[0]][self.marioPos[1]-1] != self.BLOCK):
            sonGameBoard[self.marioPos[0]][self.marioPos[1]-1] = self.MARIO
            if self.depth > 0:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]
                                               ] = self.checkNoPowerRepeat()
            else:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0], self.marioPos[1]-1)

        # MOVE TO DOWN
        elif direction == self.DOWN and (self.marioPos[0]+1 <= self.ROWS-1) and (sonGameBoard[self.marioPos[0]+1][self.marioPos[1]] != self.BLOCK):
            sonGameBoard[self.marioPos[0]+1][self.marioPos[1]] = self.MARIO
            if self.depth > 0:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]
                                               ] = self.checkNoPowerRepeat()
            else:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY

            # New Mario position
            sonMarioPosition = (self.marioPos[0]+1, self.marioPos[1])

        # MOVE TO RIGHT
        elif direction == self.RIGHT and (self.marioPos[1]+1 <= self.COLS-1) and (sonGameBoard[self.marioPos[0]][self.marioPos[1]+1] != self.BLOCK):
            sonGameBoard[self.marioPos[0]][self.marioPos[1]+1] = self.MARIO
            if self.depth > 0:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]
                                               ] = self.checkNoPowerRepeat()
            else:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY

            # New Mario position
            sonMarioPosition = (self.marioPos[0], self.marioPos[1]+1)

        # MOVE TO UP
        elif direction == self.UP and (self.marioPos[0]-1 >= 0) and (sonGameBoard[self.marioPos[0]-1][self.marioPos[1]] != self.BLOCK):
            sonGameBoard[self.marioPos[0]-1][self.marioPos[1]] = self.MARIO
            if self.depth > 0:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]
                                               ] = self.checkNoPowerRepeat()
            else:
                sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY

            # New Mario position
            sonMarioPosition = (self.marioPos[0]-1, self.marioPos[1])

        return sonGameBoard, sonMarioPosition

    def showDepth(self):
        print("La profundidad del nodo es:", self.depth)

    def showOperator(self):
        print("El operador usado fue:", self.operator)

    def showgameBoard(self):
        print(self.gameBoard)

    def goalReached(self, yoshiPos):
        return self.marioPos == yoshiPos

    def checkPowerUps(self):

        if self.gameCharacter == self.FLOWER and self.star_effect == 0:
            self.flowers_acum += self.BULLETS
        if self.gameCharacter == self.STAR and self.flowers_acum == 0:
            if self.star_effect > 0:
                self.star_effect += self.STAR_POWER
            else:
                self.star_effect += self.STAR_POWER + 1

    # checkCost: int
    # returns the cost of the movement that has been done
    def checkCost(self):

        if self.getStar_effect() > 0:
            return self.MOVE_WITH_STAR_COST
        else:

            if self.gameCharacter == self.EMPTY:
                return self.MOVE_COST
            if self.gameCharacter == self.KOOPA:
                if self.flowers_acum > 0:
                    return self.MOVE_COST
                else:
                    return self.MOVE_COST + self.KOOPA
            if self.gameCharacter == self.FLOWER:
                return self.MOVE_COST
            if self.gameCharacter == self.STAR:
                return self.MOVE_COST
            if self.gameCharacter == self.YOSHI:
                return self.MOVE_COST

    # spendPowerUps:
    # This function check the necesary spends by actions
    def spendPowerUps(self):

        if self.flowers_acum > 0:
            if self.gameCharacter == self.KOOPA:
                self.flowers_acum -= 1

        if self.star_effect > 0:
            self.star_effect -= 1

# CHANGE FUNCION NAME
# checkNoPowerRepeat:
# This functions checks what element was in the position that Mario occupies now and determines if that element
# should stay or be removed (replaced by empty)
    def checkNoPowerRepeat(self):

        flowersFatherHad = self.father.getFlower_acum()
        starsFatherHad = self.father.getStar_effect()
        if self.gameCharacter == self.STAR and flowersFatherHad > 0:
            return self.STAR
        elif self.gameCharacter == self.FLOWER and starsFatherHad > 0:
            return self.FLOWER
        elif self.gameCharacter == self.KOOPA and flowersFatherHad == 0 and starsFatherHad == 0:  # ADDED
            return self.KOOPA
        else:
            return self.EMPTY

    # Heuristic
    # Manhattan distance
    def getHeuristic(self):
        distance_x = abs(self.marioPos[0] - self.yoshiPos[0])
        distance_y = abs(self.marioPos[1] - self.yoshiPos[1])
        distance = (distance_x + distance_y)/2
        return distance

    def getBest(self):
        return self.getHeuristic() + self.getCost()
