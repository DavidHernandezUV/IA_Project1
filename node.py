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

    def __init__(self, gameBoard, father, operator, depth, cost, marioPos):
        self.gameBoard = gameBoard
        self.father = father
        self.operator = operator
        self.depth = depth
        self.ROWS = len(gameBoard)
        self.COLS = len(gameBoard[0])
        self.marioPos = marioPos
        self.cost = cost

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

        return sonGameBoard, sonMarioPosition

    def showDepth(self):
        print("La profundidad del nodo es:", self.depth)

    def showOperator(self):
        print("El operador usado fue:", self.operator)

    def showgameBoard(self):
        print(self.gameBoard)

    def goalReached(self, yoshiPos):
        return self.marioPos == yoshiPos
