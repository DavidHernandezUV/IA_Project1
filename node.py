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

    def __init__(self, gameBoard, father, operator, depth, marioPos):
        self.gameBoard = gameBoard
        self.father = father
        self.operator = operator
        self.depth = depth
        self.ROWS = len(gameBoard)
        self.COLS = len(gameBoard[0])
        self.marioPos = marioPos

        if depth == 0:
            self.cost = 0
            self.flowers_acum = 0
            self.star_effect = 0
        else:

            self.star_effect = father.getStar_effect()
            self.flowers_acum = father.getFlower_effect()
            self.cost = father.getCost() + self.checkCost()
            # should spend before taking any a powerup
            self.spendPowerUps()
            self.checkPowerUps()

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
        return self.koopasPos

    def getStar_effect(self):
        return self.star_effect

    def getFlower_effect(self):
        return self.flowers_acum
    # move: number -> matrix, tuple
    # Checks if it is possible to move in a given direction (not going through block or limit)

    def move(self, direction):

        # create copied son
        sonGameBoard = np.array(self.gameBoard, copy=True)
        sonMarioPosition = self.marioPos
        cost = 0
        flowers_acum = 0
        star_effect = 0
        # Checks if there is no limit or block
        # MOVE TO LEFT
        if direction == self.LEFT and (self.marioPos[1]-1 >= 0) and (sonGameBoard[self.marioPos[0]][self.marioPos[1]-1] != self.BLOCK):
            sonGameBoard[self.marioPos[0]][self.marioPos[1]-1] = self.MARIO
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0], self.marioPos[1]-1)

        # MOVE TO DOWN
        elif direction == self.DOWN and (self.marioPos[0]+1 <= self.ROWS-1) and (sonGameBoard[self.marioPos[0]+1][self.marioPos[1]] != self.BLOCK):
            sonGameBoard[self.marioPos[0]+1][self.marioPos[1]] = self.MARIO
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0]+1, self.marioPos[1])

        # MOVE TO RIGHT
        elif direction == self.RIGHT and (self.marioPos[1]+1 <= self.COLS-1) and (sonGameBoard[self.marioPos[0]][self.marioPos[1]+1] != self.BLOCK):
            sonGameBoard[self.marioPos[0]][self.marioPos[1]+1] = self.MARIO
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0], self.marioPos[1]+1)

        # MOVE TO UP
        elif direction == self.UP and (self.marioPos[0]-1 >= 0) and (sonGameBoard[self.marioPos[0]-1][self.marioPos[1]] != self.BLOCK):
            sonGameBoard[self.marioPos[0]-1][self.marioPos[1]] = self.MARIO
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
        gameCharacter = self.father.getGameBoard()[self.marioPos]
        if gameCharacter == self.FLOWER and self.star_effect == 0:
            self.flowers_acum += self.BULLETS
        if gameCharacter == self.STAR and self.flowers_acum == 0:
            self.star_effect += self.STAR_POWER

    # checkCost: int
    # returns the cost of the movement that has been done
    def checkCost(self):
        gameCharacter = self.father.getGameBoard()[self.marioPos]

        if self.getStar_effect() > 0:
            return self.MOVE_WITH_STAR_COST
        else:

            if gameCharacter == self.EMPTY:
                return self.MOVE_COST
            if gameCharacter == self.KOOPA:
                if self.flowers_acum > 0:
                    return self.MOVE_COST
                else:
                    return self.MOVE_COST + self.KOOPA
            if gameCharacter == self.FLOWER:
                return self.MOVE_COST
            if gameCharacter == self.STAR:
                return self.MOVE_COST
            if gameCharacter == self.YOSHI:
                return self.MOVE_COST

    # spendPowerUps:
    # This function check the necesary spends by actions
    def spendPowerUps(self):

        gameCharacter = self.father.getGameBoard()[self.marioPos]
        if self.flowers_acum > 0:
            if gameCharacter == self.KOOPA:
                self.flowers_acum -= 1

        if self.star_effect > 0:
            self.star_effect -= 1
