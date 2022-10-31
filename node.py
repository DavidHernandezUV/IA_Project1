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

    def __init__(self, gameBoard, father, operator, depth, cost, marioPos, starsPos, flowersPos, koopasPos, flowers_acum, star_effect):
        self.gameBoard = gameBoard
        self.father = father
        self.operator = operator
        self.depth = depth
        self.ROWS = len(gameBoard)
        self.COLS = len(gameBoard[0])
        self.marioPos = marioPos
        self.cost = cost
        self.starsPos = starsPos
        self.flowersPos = flowersPos
        self.koopasPos = koopasPos
        self.flowers_acum = flowers_acum
        self.star_effect = star_effect

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

    def getStarsPos(self):
        return self.starsPos

    def getFlowersPos(self):
        return self.flowersPos

    def getKoopasPos(self):
        return self.koopasPos

    def getStar_effect(self):
        return self.star_effect

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
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0], self.marioPos[1]-1)

        # MOVE TO DOWN
        if direction == self.DOWN and (self.marioPos[0]+1 <= self.ROWS-1) and (sonGameBoard[self.marioPos[0]+1][self.marioPos[1]] != self.BLOCK):
            sonGameBoard[self.marioPos[0]+1][self.marioPos[1]] = self.MARIO
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0]+1, self.marioPos[1])
        # MOVE TO RIGHT
        if direction == self.RIGHT and (self.marioPos[1]+1 <= self.COLS-1) and (sonGameBoard[self.marioPos[0]][self.marioPos[1]+1] != self.BLOCK):
            sonGameBoard[self.marioPos[0]][self.marioPos[1]+1] = self.MARIO
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0], self.marioPos[1]+1)
        # MOVE TO UP
        if direction == self.UP and (self.marioPos[0]-1 >= 0) and (sonGameBoard[self.marioPos[0]-1][self.marioPos[1]] != self.BLOCK):
            sonGameBoard[self.marioPos[0]-1][self.marioPos[1]] = self.MARIO
            sonGameBoard[self.marioPos[0]][self.marioPos[1]] = self.EMPTY
            # New Mario position
            sonMarioPosition = (self.marioPos[0]-1, self.marioPos[1])

        # Checks if it can pick up a power up
        flowers_acum, star_effect = self.checkPowerUps(sonMarioPosition)
        # Find the cost of the new position
        cost = self.checkCost(sonMarioPosition)
        return sonGameBoard, sonMarioPosition, cost, flowers_acum, star_effect

    def showDepth(self):
        print("La profundidad del nodo es:", self.depth)

    def showOperator(self):
        print("El operador usado fue:", self.operator)

    def showgameBoard(self):
        print(self.gameBoard)

    def goalReached(self, yoshiPos):
        return self.marioPos == yoshiPos

    def checkPowerUps(self, sonMarioPosition):
        gameCharacter = self.gameBoard[sonMarioPosition]
        if gameCharacter == self.FLOWER and self.star_effect == 0:
            self.flowers_acum += self.BULLETS
        if gameCharacter == self.STAR and self.flowers_acum == 0:
            self.star_effect += self.STAR_POWER
            print("Cogí una estrella", self.star_effect)
        return self.flowers_acum, self.star_effect

    def checkCost(self, sonMarioPosition):
        gameCharacter = self.gameBoard[sonMarioPosition]
        if self.star_effect > 0:
            self.star_effect -= 1
            return self.MOVE_WITH_STAR_COST
        else:
            # Check if the new Mario position is empty
            if gameCharacter == self.EMPTY:
                return self.MOVE_COST
            if gameCharacter == self.KOOPA:
                return self.MOVE_COST + self.KOOPA
            if gameCharacter == self.FLOWER:
                return self.MOVE_COST
            if gameCharacter == self.STAR:
                return self.MOVE_COST
            if gameCharacter == self.YOSHI:
                return self.MOVE_COST
